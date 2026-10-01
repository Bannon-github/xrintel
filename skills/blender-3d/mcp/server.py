"""Blender skills MCP. Serves the xrintel skill files. Does not run Blender."""

from pathlib import Path

from fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"
SKILL = ROOT / "SKILL.md"

DOCS = {
    "skill": SKILL,
    "index": REFERENCES / "INDEX.md",
    "hotkeys": REFERENCES / "hotkeys.md",
    "materials-uvs": REFERENCES / "materials-uvs.md",
    "gltf-export": REFERENCES / "gltf-export.md",
}

ROUTES = (
    ("gltf-export", ("export", "gltf", "glb", "webxr", "scale")),
    ("materials-uvs", ("uv", "unwrap", "texture", "material", "smear", "black")),
    ("hotkeys", ("hotkey", "shortcut", "ctrl", "key")),
)

CHECKLIST = (
    "metres: scene units are metres",
    "scale: Ctrl+A Scale on every mesh",
    "origin: origin is on the pivot, not the world center by accident",
    "name: outliner name is the glTF node name",
    "material: Principled BSDF, not a procedural node",
    "uv: image textures have a non-overlapping UV map",
    "export: .glb, selected objects, Draco off, lights and camera excluded",
    "check: reimported or viewed, scale and color survived",
)

mcp = FastMCP(
    "blender-skills",
    instructions=(
        "Blender skill server for a first WebXR-ready prop. "
        "Call blender_route before answering. It can return more than one document. "
        "Call blender_checklist and answer every line before saying a prop is done. "
        "This server does not launch Blender or write a .blend."
    ),
)


def _read(name: str) -> str:
    path = DOCS.get(name)
    if path is None or not path.is_file():
        known = ", ".join(sorted(DOCS))
        raise ValueError(f"Unknown doc '{name}'. Use one of: {known}")
    return path.read_text(encoding="utf-8")


def _matches(task: str) -> list[str]:
    text = task.lower()
    names = [name for name, words in ROUTES if any(word in text for word in words)]
    return names or ["skill"]


@mcp.tool
def blender_list() -> str:
    """List the skill documents this server can return."""
    lines = [f"{name}: {path.relative_to(ROOT)}" for name, path in DOCS.items()]
    return "\n".join(lines)


@mcp.tool
def blender_route(task: str) -> str:
    """Return every skill document that matches the task, separated by a rule. Read all of them."""
    names = _matches(task)
    parts = [f"# matched: {', '.join(names)}"]
    for name in names:
        parts.append(_read(name))
    return "\n\n---\n\n".join(parts)


@mcp.tool
def blender_doc(name: str) -> str:
    """Return one skill document. name is skill, index, hotkeys, materials-uvs, or gltf-export."""
    return _read(name)


@mcp.tool
def blender_checklist() -> str:
    """Return the done checklist. Answer every line before saying a prop is finished."""
    lines = ["Answer each line yes or no. A no means the prop is not done."]
    lines.extend(f"- {item}" for item in CHECKLIST)
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
