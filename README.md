# Pythonプロジェクト
# Python Project

このリポジトリはPythonプロジェクトのボイラープレートです。
This repository is a boilerplate for Python projects.

## 機能 / Features

- setuptoolsを使用したシンプルなパッケージング
  (Simple packaging using setuptools)
- src/とtests/ディレクトリによる構造化
  (Structured with src/ and tests/ directories)
- メインプログラムのエントリーポイント
  (Main program entry point)
- pytestを使用したテスト例
  (Test examples using pytest)
- Dockerによる開発環境のサポート
  (Docker development environment support)

## 使い方 / Usage

メインプログラムの実行 / Run main program:

```bash
python -m my_project.main
```

### Dockerを使用する場合 / Using Docker

開発環境をDockerで構築することもできます。
You can also set up the development environment using Docker.

1. 開発環境の起動 / Start development environment:
```bash
docker compose up -d
```

2. コンテナ内でコマンドを実行 / Execute commands in container:
```bash
# コンテナのシェルにアクセス / Access container shell
docker compose exec app /bin/bash
```

3. 開発環境の停止 / Stop development environment:
```bash
docker compose down
```

## テスト / Tests

テストの実行 / Run tests:
```bash
pytest
```

### Dockerでのテスト実行 / Running tests in Docker

コンテナ内でテストを実行 / Run tests in container:
```bash
docker compose exec app pytest
```
