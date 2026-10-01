# xrintel
XR Intel — intelligent WebXR / spatial web experiments by Matthew Bannon (Xrintel). Home of xrintel.ca.

## Blender skills MCP

The Blender skill is an MCP server, not a Blender script. It serves the lesson files so an agent can follow them. It does not open Blender or write a `.blend`.

- Skill: [skills/blender-3d/SKILL.md](skills/blender-3d/SKILL.md)
- Server: [skills/blender-3d/mcp/server.py](skills/blender-3d/mcp/server.py)
- Tools: `blender_route`, `blender_doc`, `blender_project`, `blender_list`

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

Requires `pip install -r skills/blender-3d/mcp/requirements.txt` and a working directory at the repo root. Agent entry: [AGENTS.md](AGENTS.md).
