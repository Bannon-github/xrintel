# Agents

If the task is Blender, a 3D prop, UVs, materials, or a glTF/WebXR asset, use the blender-skills MCP. It serves `skills/blender-3d/` and does not launch Blender.

Connect stdio:

```json
{
  "mcpServers": {
    "blender-skills": {
      "command": "python",
      "args": ["skills/blender-3d/mcp/server.py"]
    }
  }
}
```

Install `fastmcp` first (`pip install -r skills/blender-3d/mcp/requirements.txt`). Call `blender_route` with the task before answering. Read every document it returns. Call `blender_checklist` and answer every line before saying a prop is done. If the MCP is not connected, read `skills/blender-3d/SKILL.md` instead.
