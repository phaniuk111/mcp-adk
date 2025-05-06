#!/usr/bin/env python3
# gcloud_tool.py

import sys
import asyncio
import subprocess
import shlex
import time
from typing import Tuple, Dict, Any


class GcloudTool:
    """
    Wraps 'gcloud' shell commands in an async class.

    Usage (async):
        tool = GcloudTool(debug=True)
        success, out, err = await tool.run("gcloud projects list --format=json")

    Usage (sync):
        tool = GcloudTool(debug=False)
        result = tool.run_sync("gcloud projects list --format=json")
        # result == {"success": bool, "stdout": str, "stderr": str}
    """

    def __init__(self, debug: bool = True):
        self.debug = debug

    @classmethod
    def initialize(cls, debug: bool = True) -> "GcloudTool":
        """
        Alternate constructor if you prefer a named initializer.
        """
        return cls(debug=debug)

    async def _run(self, cmd: str) -> subprocess.CompletedProcess:
        """
        Internal helper: run any shell command asynchronously,
        capturing stdout/stderr and logging timing if debug=True.
        """
        if self.debug:
            print(f"[DBG] ➜ {cmd}")
        start = time.monotonic()
        proc = await asyncio.to_thread(
            subprocess.run,
            shlex.split(cmd),
            capture_output=True,
            text=True,
        )
        elapsed = time.monotonic() - start
        if self.debug:
            print(f"[DBG] ↲ return={proc.returncode} time={elapsed:.2f}s")
        return proc

    async def run(self, cmd: str) -> Tuple[bool, str, str]:
        """
        Execute any `gcloud …` command asynchronously.
        Returns a tuple: (success: bool, stdout: str, stderr: str).
        Rejects anything not starting with 'gcloud'.
        """
        if not cmd.strip().lower().startswith("gcloud"):
            return False, "", "Error: Only 'gcloud' commands are allowed"
        proc = await self._run(cmd)
        return proc.returncode == 0, proc.stdout, proc.stderr

    def run_sync(self, cmd: str) -> Dict[str, Any]:
        """
        Synchronous wrapper around the async .run(...) method.
        Usage from a non-async context.
        """
        success, out, err = asyncio.run(self.run(cmd))
        return {"success": success, "stdout": out, "stderr": err}


# Example standalone usage:
if __name__ == "__main__":
    tool = GcloudTool.initialize(debug=True)

    if len(sys.argv) < 2:
        print("Usage: gcloud_tool.py \"gcloud <your-command>\"")
        sys.exit(1)

    # Combine all CLI args into the full command string
    cmd = " ".join(sys.argv[1:])
    result = tool.run_sync(cmd)

    if result["success"]:
        print("\n✅ Command succeeded")
        print(result["stdout"])
    else:
        print("\n❌ Command failed:")
        print(result["stderr"])