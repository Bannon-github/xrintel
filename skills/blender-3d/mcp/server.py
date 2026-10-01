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
    "projects": REFERENCES / "projects.md",
}

mcp = FastMCP(
    "blender-skills",
    instructions=(
        "Blender skill server for a first WebXR-ready prop. "
        "Call blender_route before answering a Blender, UV, material, or glTF question. "
        "This server does not launch Blender or write a .blend."
    ),
)


def _read(name: str) -> str:
    path = DOCS.get(name)
    if path is None or not path.is_file():
        known = ", ".join(sorted(DOCS))
        raise ValueError(f"Unknown doc '{name}'. Use one of: {known}")
    return path.read_text(encoding="utf-8")


def _section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    if start < 0:
        raise ValueError(f"No section '{heading}' in projects.md")
    rest = text[start + len(marker) :]
    nxt = rest.find("\n## ")
    body = rest if nxt < 0 else rest[:nxt]
    return marker + "\n" + body.strip() + "\n"


@mcp.tool
def blender_list() -> str:
    """List the skill documents this server can return."""
    lines = [f"{name}: {path.relative_to(ROOT)}" for name, path in DOCS.items()]
    return "\n".join(lines)


@mcp.tool
def blender_route(task: str) -> str:
    """Return the skill document that matches a Blender task. Read this before answering."""
    text = task.lower()
    if any(word in text for word in ("export", "gltf", "glb", "webxr", "scale")):
        name = "gltf-export"
    elif any(word in text for word in ("uv", "unwrap", "texture", "material", "smear", "black")):
        name = "materials-uvs"
    elif any(word in text for word in ("hotkey", "shortcut", "ctrl", "key")):
        name = "hotkeys"
    elif any(word in text for word in ("vase", "mug", "donut", "flower", "low-poly", "low poly", "joey", "poole", "guru")):
        name = "projects"
    else:
        name = "skill"
    return _read(name)


@mcp.tool
def blender_doc(name: str) -> str:
    """Return one skill document. name is skill, index, hotkeys, materials-uvs, gltf-export, or projects."""
    return _read(name)


@mcp.tool
def blender_project(exercise: str) -> str:
    """Return one exercise: vase, scene, or mug."""
    key = exercise.lower()
    heading = {
        "vase": "Vase (Poole)",
        "poole": "Vase (Poole)",
        "scene": "Low-poly scene (Joey Carlino)",
        "low-poly": "Low-poly scene (Joey Carlino)",
        "joey": "Low-poly scene (Joey Carlino)",
        "mug": "Mug, donut part 1 (Blender Guru)",
        "donut": "Mug, donut part 1 (Blender Guru)",
        "guru": "Mug, donut part 1 (Blender Guru)",
    }.get(key)
    if heading is None:
        raise ValueError("exercise must be vase, scene, or mug")
    return _section(_read("projects"), heading)


if __name__ == "__main__":
    mcp.run()
