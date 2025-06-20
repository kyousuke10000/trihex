# 🌐 Cloudflare → GAS 中継Worker

このフォルダは、Truthsphereワーク診断の記入データをGoogle Apps Scriptに中継するCloudflare Workerを管理しています。

## 使用ファイル

- `Cloudflare_to_GAS.js`：GAS中継Worker本体
- `sample_request_gas.json`：GAS POSTテスト用データ

## 中継先

`https://script.google.com/macros/s/.../exec`
