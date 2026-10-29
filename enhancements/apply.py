from pathlib import Path

RULE = "enhancements/research-and-writing.md"

def patch_file(path, marker, header, insert):
    content = path.read_text(encoding="utf-8")
    if header in content:
        return
    if marker not in content:
        raise ValueError(f"Expected marker missing in {path}")
    path.write_text(content.replace(marker, insert + "\n" + marker, 1), encoding="utf-8")

def main():
    root = Path(".")
    if not (root / "skills/patent-disclosure/SKILL.md").exists():
        raise RuntimeError("Must first import the full upstream repository")
    patch_file(root / "SKILL.md", "## 执行前核对",
        "## Codex 增强规范",
        "## Codex 增强规范\n\n在交底、申请文件及审核任务中必须读取 " + RULE +
        "，核查技术证据、检索出处、保密及中文表达。不虚构技术事实。")
    for name in ("patent-disclosure", "patent-application", "patent-docket"):
        patch_file(root / "skills" / name / "SKILL.md", "## 护栏",
            "## 研发材料质量规范",
            "## 研发材料质量规范\n\n成文及终审时必须读取仓库根目录 " + RULE +
            "，执行事实追溯、检索来源核查、简洁中文写作和交付检查。")
    Path("ENHANCEMENT_NOTES.md").write_text(
        "基于 handsomestWei/patent-disclosure-skill，遵循原 MIT License。"
        "本版增加研发事实、检索与文风要求；专业人员应复核申请底稿。\n",
        encoding="utf-8")

if __name__ == "__main__":
    main()
