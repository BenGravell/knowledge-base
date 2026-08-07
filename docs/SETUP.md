# Setup

You need `git` plus `curl` or `wget`.

The `./dev` wrapper installs Pixi locally on first use, then uses the checked-in `pixi.lock`.

```bash
./dev install
```

## VS Code

VS Code recommends Pixi Code plus the Python extensions.

Pixi Code follows the upstream extension behavior: it auto-discovers `pixi` on
`PATH`, then registers the `knowledge-base:default` environment after
`./dev install` creates `.pixi/envs/default`.
If VS Code does not select it automatically, choose that Pixi environment manually.
