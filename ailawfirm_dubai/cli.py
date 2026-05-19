#!/usr/bin/env python3
"""
AI Law Firm — Dubai-DIFC · Solo Edition · v0.1
================================================
Dual-system practice OS: DIFC (offshore common-law English) + Dubai Mainland (onshore civil-law Arabic)
5-language Gulf support: English · العربية · اردو · हिन्दी · Tagalog

Commands:
    ailawfirm-dubai init <dir> --system difc|mainland|both
    ailawfirm-dubai mine <dir>
    ailawfirm-dubai search "query"
    ailawfirm-dubai wake-up
    ailawfirm-dubai status
    ailawfirm-dubai split <dir>
    ailawfirm-dubai compress
"""

import os
import sys
import argparse
from pathlib import Path

from .config import AILawFirmDubaiConfig


def cmd_init(args):
    import json
    from pathlib import Path
    from .entity_detector import scan_for_detection, detect_entities, confirm_entities
    from .room_detector_local import detect_rooms_local

    # Pass 1: auto-detect people and projects from file content
    print(f"\n  Scanning for entities in: {args.dir}")
    files = scan_for_detection(args.dir)
    if files:
        print(f"  Reading {len(files)} files...")
        detected = detect_entities(files)
        total = len(detected["people"]) + len(detected["projects"]) + len(detected["uncertain"])
        if total > 0:
            confirmed = confirm_entities(detected, yes=getattr(args, "yes", False))
            # Save confirmed entities to <project>/entities.json for the miner
            if confirmed["people"] or confirmed["projects"]:
                entities_path = Path(args.dir).expanduser().resolve() / "entities.json"
                with open(entities_path, "w") as f:
                    json.dump(confirmed, f, indent=2)
                print(f"  Entities saved: {entities_path}")
        else:
            print("  No entities detected — proceeding with directory-based rooms.")

    # Pass 2: detect rooms from folder structure
    detect_rooms_local(project_dir=args.dir)
    AILawFirmDubaiConfig().init()


def cmd_mine(args):
    palace_path = (
        os.path.expanduser(args.palace) if args.palace else AILawFirmDubaiConfig().palace_path
    )

    if args.mode == "convos":
        from .convo_miner import mine_convos

        mine_convos(
            convo_dir=args.dir,
            palace_path=palace_path,
            wing=args.wing,
            agent=args.agent,
            limit=args.limit,
            dry_run=args.dry_run,
            extract_mode=args.extract,
        )
    else:
        from .miner import mine

        mine(
            project_dir=args.dir,
            palace_path=palace_path,
            wing_override=args.wing,
            agent=args.agent,
            limit=args.limit,
            dry_run=args.dry_run,
        )


def cmd_search(args):
    from .searcher import search

    palace_path = (
        os.path.expanduser(args.palace) if args.palace else AILawFirmDubaiConfig().palace_path
    )
    search(
        query=args.query,
        palace_path=palace_path,
        wing=args.wing,
        room=args.room,
        n_results=args.results,
    )


def cmd_wakeup(args):
    """Show L0 (identity) + L1 (essential story) — the wake-up context."""
    from .layers import MemoryStack

    palace_path = (
        os.path.expanduser(args.palace) if args.palace else AILawFirmDubaiConfig().palace_path
    )
    stack = MemoryStack(palace_path=palace_path)

    text = stack.wake_up(wing=args.wing)
    tokens = len(text) // 4
    print(f"Wake-up text (~{tokens} tokens):")
    print("=" * 50)
    print(text)


def cmd_split(args):
    """Split concatenated transcript mega-files into per-session files."""
    from .split_mega_files import main as split_main
    import sys

    # Rebuild argv for split_mega_files argparse
    argv = [args.dir]
    if args.output_dir:
        argv += ["--output-dir", args.output_dir]
    if args.dry_run:
        argv.append("--dry-run")
    if args.min_sessions != 2:
        argv += ["--min-sessions", str(args.min_sessions)]

    old_argv = sys.argv
    sys.argv = ["ailawfirm_dubai split"] + argv
    try:
        split_main()
    finally:
        sys.argv = old_argv


def cmd_status(args):
    from .miner import status

    palace_path = (
        os.path.expanduser(args.palace) if args.palace else AILawFirmDubaiConfig().palace_path
    )
    status(palace_path=palace_path)


def cmd_compress(args):
    """Compress drawers in a wing using Entity-Aliasing Dialect."""
    import chromadb
    from .dialect import Dialect

    palace_path = (
        os.path.expanduser(args.palace) if args.palace else AILawFirmDubaiConfig().palace_path
    )

    # Load dialect (with optional entity config)
    config_path = args.config
    if not config_path:
        for candidate in ["entities.json", os.path.join(palace_path, "entities.json")]:
            if os.path.exists(candidate):
                config_path = candidate
                break

    if config_path and os.path.exists(config_path):
        dialect = Dialect.from_config(config_path)
        print(f"  Loaded entity config: {config_path}")
    else:
        dialect = Dialect()

    # Connect to palace
    try:
        client = chromadb.PersistentClient(path=palace_path)
        col = client.get_collection("ailawfirm_dubai_drawers")
    except Exception:
        print(f"\n  No palace found at {palace_path}")
        print("  Run: ailawfirm-dubai init <dir> then ailawfirm-dubai mine <dir>")
        sys.exit(1)

    # Query drawers in the wing
    where = {"wing": args.wing} if args.wing else None
    try:
        kwargs = {"include": ["documents", "metadatas"]}
        if where:
            kwargs["where"] = where
        results = col.get(**kwargs)
    except Exception as e:
        print(f"\n  Error reading drawers: {e}")
        sys.exit(1)

    docs = results["documents"]
    metas = results["metadatas"]
    ids = results["ids"]

    if not docs:
        wing_label = f" in wing '{args.wing}'" if args.wing else ""
        print(f"\n  No drawers found{wing_label}.")
        return

    print(
        f"\n  Compressing {len(docs)} drawers"
        + (f" in wing '{args.wing}'" if args.wing else "")
        + "..."
    )
    print()

    total_original = 0
    total_compressed = 0
    compressed_entries = []

    for doc, meta, doc_id in zip(docs, metas, ids):
        compressed = dialect.compress(doc, metadata=meta)
        stats = dialect.compression_stats(doc, compressed)

        total_original += stats["original_chars"]
        total_compressed += stats["compressed_chars"]

        compressed_entries.append((doc_id, compressed, meta, stats))

        if args.dry_run:
            wing_name = meta.get("wing", "?")
            room_name = meta.get("room", "?")
            source = Path(meta.get("source_file", "?")).name
            print(f"  [{wing_name}/{room_name}] {source}")
            print(
                f"    {stats['original_tokens']}t -> {stats['compressed_tokens']}t ({stats['ratio']:.1f}x)"
            )
            print(f"    {compressed}")
            print()

    # Store compressed versions (unless dry-run)
    if not args.dry_run:
        try:
            comp_col = client.get_or_create_collection("ailawfirm_dubai_compressed")
            for doc_id, compressed, meta, stats in compressed_entries:
                comp_meta = dict(meta)
                comp_meta["compression_ratio"] = round(stats["ratio"], 1)
                comp_meta["original_tokens"] = stats["original_tokens"]
                comp_col.upsert(
                    ids=[doc_id],
                    documents=[compressed],
                    metadatas=[comp_meta],
                )
            print(
                f"  Stored {len(compressed_entries)} compressed drawers in 'mempalace_compressed' collection."
            )
        except Exception as e:
            print(f"  Error storing compressed drawers: {e}")
            sys.exit(1)

    # Summary
    ratio = total_original / max(total_compressed, 1)
    orig_tokens = Dialect.count_tokens("x" * total_original)
    comp_tokens = Dialect.count_tokens("x" * total_compressed)
    print(f"  Total: {orig_tokens:,}t -> {comp_tokens:,}t ({ratio:.1f}x compression)")
    if args.dry_run:
        print("  (dry run -- nothing stored)")


WELCOME_BANNER = r"""
═══════════════════════════════════════════════════════════════════
  AI Law Firm — Dubai-DIFC · Solo Edition · v0.1

  🙏 Welcome · أهلاً وسهلاً · خوش آمدید · स्वागत · Mabuhay
═══════════════════════════════════════════════════════════════════
  DIFC (offshore common-law) + Dubai Mainland (onshore civil-law)
  Pick: ailawfirm-dubai init --system difc|mainland|both
═══════════════════════════════════════════════════════════════════
  Built on MemPalace (MIT — github.com/mempalace/mempalace)
  Published by Wolfgang_rush · $0 forever · your data stays here
  https://github.com/Wolfgangrush/ai-law-firm-dubai
═══════════════════════════════════════════════════════════════════
"""


def _print_welcome():
    """Print welcome banner. Called when running with no arguments."""
    print(WELCOME_BANNER)
    print(
        "  This is YOUR practice OS for Dubai. No cloud. No subscription.\n"
        "  One City, Two Systems — DIFC + Mainland in one tool.\n"
    )
    print("  Quick start:")
    print("    ailawfirm-dubai init --system difc <your-matters-dir>")
    print("    ailawfirm-dubai mine <your-matters-dir>")
    print('    ailawfirm-dubai search "<query>"')
    print()
    print("  Read GETTING_STARTED.md (also العربية, اردو, हिन्दी, Tagalog)")
    print("  in 5 languages for Gulf legal community.\n")


def main():
    if len(sys.argv) == 1:
        _print_welcome()
        sys.exit(0)

    parser = argparse.ArgumentParser(
        description="AI Law Firm Dubai-DIFC — dual-system practice OS for UAE solo advocates. "
        "Built on MemPalace (MIT). Published by Wolfgang_rush.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--palace",
        default=None,
        help="Where the palace lives (default: from ~/.ailawfirm-dubai/config.json or ~/.ailawfirm-dubai/palace)",
    )

    sub = parser.add_subparsers(dest="command")

    # init
    p_init = sub.add_parser("init", help="Detect rooms from your folder structure")
    p_init.add_argument("dir", help="Project directory to set up")
    p_init.add_argument(
        "--system",
        choices=["difc", "mainland", "both"],
        default="both",
        help="Legal system: difc (offshore common-law), mainland (onshore civil-law), both (default)",
    )
    p_init.add_argument(
        "--yes", action="store_true", help="Auto-accept all detected entities (non-interactive)"
    )

    # mine
    p_mine = sub.add_parser("mine", help="Mine files into the palace")
    p_mine.add_argument("dir", help="Directory to mine")
    p_mine.add_argument(
        "--mode",
        choices=["projects", "convos"],
        default="projects",
        help="Ingest mode: 'projects' for code/docs (default), 'convos' for chat exports",
    )
    p_mine.add_argument("--wing", default=None, help="Wing name (default: directory name)")
    p_mine.add_argument(
        "--agent",
        default="ailawfirm-dubai",
        help="Your name — recorded on every drawer (default: ailawfirm-dubai)",
    )
    p_mine.add_argument("--limit", type=int, default=0, help="Max files to process (0 = all)")
    p_mine.add_argument(
        "--dry-run", action="store_true", help="Show what would be filed without filing"
    )
    p_mine.add_argument(
        "--extract",
        choices=["exchange", "general"],
        default="exchange",
        help="Extraction strategy for convos mode: 'exchange' (default) or 'general' (5 memory types)",
    )

    # search
    p_search = sub.add_parser("search", help="Find anything, exact words")
    p_search.add_argument("query", help="What to search for")
    p_search.add_argument("--wing", default=None, help="Limit to one project")
    p_search.add_argument("--room", default=None, help="Limit to one room")
    p_search.add_argument("--results", type=int, default=5, help="Number of results")

    # compress
    p_compress = sub.add_parser(
        "compress", help="Compress drawers using Entity-Aliasing Dialect (~30x reduction)"
    )
    p_compress.add_argument("--wing", default=None, help="Wing to compress (default: all wings)")
    p_compress.add_argument(
        "--dry-run", action="store_true", help="Preview compression without storing"
    )
    p_compress.add_argument(
        "--config", default=None, help="Entity config JSON (e.g. entities.json)"
    )

    # wake-up
    p_wakeup = sub.add_parser("wake-up", help="Show L0 + L1 wake-up context (~600-900 tokens)")
    p_wakeup.add_argument("--wing", default=None, help="Wake-up for a specific project/wing")

    # split
    p_split = sub.add_parser(
        "split",
        help="Split concatenated transcript mega-files into per-session files (run before mine)",
    )
    p_split.add_argument("dir", help="Directory containing transcript files")
    p_split.add_argument(
        "--output-dir",
        default=None,
        help="Write split files here (default: same directory as source files)",
    )
    p_split.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be split without writing files",
    )
    p_split.add_argument(
        "--min-sessions",
        type=int,
        default=2,
        help="Only split files containing at least N sessions (default: 2)",
    )

    # status
    sub.add_parser("status", help="Show what's been filed")

    p_connect = sub.add_parser(
        "connect-local",
        help="One-command setup: install Ollama + download Qwen3 + write config (local-AI, zero cloud)",
    )
    p_connect.add_argument("--yes", "-y", action="store_true", help="skip confirmation prompts")
    p_connect.add_argument("--model", help="override the recommended model (e.g. qwen3:7b)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    from .connect_local import cmd_connect_local

    dispatch = {
        "init": cmd_init,
        "mine": cmd_mine,
        "split": cmd_split,
        "search": cmd_search,
        "compress": cmd_compress,
        "wake-up": cmd_wakeup,
        "status": cmd_status,
        "connect-local": cmd_connect_local,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
