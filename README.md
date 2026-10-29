# Patent Skill — Codex 增强版

本项目基于 [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill)（MIT License），保留上游许可与署名。

新增研发代码证据追溯、现有技术检索边界、保密和简洁中文写作规则。

## 初始化状态

首次提交会触发 GitHub Actions 导入完整上游并应用增强。请确认 Actions 成功、仓库包含根目录 SKILL.md 与 skills/patent-disclosure/SKILL.md，才进行安装。若自动导入受 GitHub 权限限制，手动执行 enhancements/apply.py。

## Codex 安装（导入成功后）

```bash
git clone https://github.com/llia731/patent-skill.git ~/.codex/patent-skill-repo
mkdir -p ~/.codex/skills
ln -s ../patent-skill-repo ~/.codex/skills/patent-disclosure-skill
```

重开 Codex 会话后，在研发项目根目录调用 `$patent-disclosure-skill`。
技术交底与申请文件需人工复核；自动检索不等于专利法律意见。
