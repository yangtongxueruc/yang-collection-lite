# -*- coding: utf-8 -*-
import json, io

P = r"C:/Users/mh/WorkBuddy/yang-collection-lite/data.json"
d = json.load(open(P, encoding="utf-8"))
d = [x for x in d if x["slug"] != "germany-lead-market-autonomous-hirte"]

body = """# 德国想领跑自动驾驶：慕尼黑拿到了 Waymo，五年 L4 法却还没跑出一辆无人车

> **来源**：The AV Market Strategist（Substack / YouTube）｜**主持**：Daniel Abreu Marques
> **嘉宾**：Christian Hirte —— 德国联邦交通部议会国务秘书（Parlamentarischer Staatssekretär），CDU 联邦议员、律师，曾任联邦政府东部事务专员
> **时长**：19:17｜**发布**：2026-11-25

> ⚠️ **本篇为「纲要＋背景导读版」**：官方页面本期未提供逐字稿（`transcription` 为空），本地亦无法取得音频，故暂无中英对照逐字稿。以下内容来自官方节目说明、章节导航与已标注来源的公开事实，**不含对访谈对话的转述**。逐字稿补齐后同 slug 增量更新。

---

## TL;DR（结论先行）

- **同一个事实，两种读法。** 2026 年 8 月 Waymo 把慕尼黑定为其**欧洲大陆首个市场**（目标 2027 年底开放商业服务），德国交通部把它读成「我们的法律框架是可落地的」；但 2021 年 L4 法生效至今，德国**没有一辆无人车进入常态化客运**。这一期就是让部委方来解释这个反差。
- **说话的人换了。** 本库上一期德国主题请的是柏林律师（外部诊断：卡在没人交出功能安全概念），这一期是**交通部政治官员**——知道卡点、也要回答「打算怎么改」。两份材料正好是「结构诊断」与「政治答辩」一对。
- **真问题不是法条完备度，而是审批吞吐。** 法规把车辆许可给了 KBA、运营区域给了各州、道路与交通管理给了市政，三方互不隶属。节目里直接问：**是否应由一个联邦机关端到端持有审批权**——这是在问德国愿不愿意为速度动一次联邦制。
- **「软件是不是欧洲的」= 德国式价值链焦虑。** 两条路被并列摆出：**技术主权**（软件必须欧洲自研，十年级投入）与**运营主权**（车队、场站、远程运营、维修岗位留在本地，三年内可见）。部委通常倾向前者表态、后者落地。
- **「欧洲版 Airbus」被当成真实政策选项。** 节目专门用一节质询：欧洲该不该像当年造 Airbus 那样用国家力量扶一个自动驾驶冠军。
- **农村与城郊是压力测试。** 商业模型弱的地方谁来服务，选项无非财政补贴、公共交通**订购**自动驾驶运力、或者承认覆盖不到。德国 ÖPNV 由州与市政出资，「订购」这条在制度上是有接口的。

---

## 章节导航（官方，中英对照）

| 时间 | 章节 | 在问什么 |
|------|------|----------|
| 1:09 | Intro | 慕尼黑的选择 vs 五年零常态运营 |
| 1:57 | Waymo picks Munich: what it says about Germany | 这个选择证明了德国法律的什么 |
| 4:13 | Why foreign players are picking Germany | 为什么是**现在** |
| 5:03 | How approvals work across KBA, Bavaria and Munich | 联邦／州／市三方怎么分审批活 |
| 6:07 | What's at stake for a car nation | 价值迁移后汽车国剩什么 |
| 8:46 | European software or local fleets and jobs? | 技术主权还是运营主权 |
| 10:49 | A European Airbus for autonomous driving? | 要不要国家扶一个冠军 |
| 11:33 | The lead market goal and the Level 4 law | 对产业界与 KBA 修法建议的态度 |
| 14:17 | Rural areas and public transport | 弱商业模型地区谁出钱 |
| 16:50 | Germany in 2035 and a message to founders | 2035 年与给创业者的话 |

---

## 事实底座（可核实）

| 事实 | 要点 | 来源 |
|------|------|------|
| Waymo 落地慕尼黑 | 2026-08-25 官宣，欧洲大陆首站；先人工测绘＋测试，目标 **2027 年底**商业开放；累计 2000 万＋无人驾驶行程、3.5 亿＋公里 | Waymo 官方博客 2026-08；electrive 2026-08-26 |
| 交通部表态 | Hirte：「法律框架我们已经建好了……Waymo 看向德国，说明无人驾驶服务在德国**常规运营是可行的**」 | 同上 |
| 法规双轨 | 2021 StVG 框架法 + 2022 AFGBV 实施细则；KBA 管车、各州管运营区域 | 本库《德国自动驾驶法》律师访谈 |
| 规则仍假设有人 | 慕尼黑交通部门承认现行规则以「车上有驾驶员」为前提，需为完全无人服务调整 | 盖世汽车 2026-08 |
| 竞争不止 Waymo | Uber＋Autobrains 慕尼黑；百度 RT6 拟 2026 年晚些接入 Lyft；Momenta、Wayve 已在德国测试 | 盖世汽车 2026-08 |

---

## 为什么值得收

1. **它是政策制定者的口径样本**：同一件事在部委口中如何被表述、哪些问题被正面回答、哪些被转成产业叙事。
2. **它把「落后」拆成可算账的两问**：审批吞吐与价值链留存——比「自主可控」的口号更能对齐真实决策。
3. **与库内两篇形成三角**：《德国自动驾驶法》（律师拆流程）、《欧洲自己的路径》（Neckermann 讲公共交通延展），加上这一篇（部委答辩）。

---

## 逐字稿状态

- 抓取时间 2026-11-25；官方 `transcription` 字段为 `null`，`?showTranscript=true` 无内容。
- 本地对 `substack.com` 全域不可达（DNS 污染＋SNI 阻断），音频与转录 CDN 直链均取不到，暂无法跑本地 ASR。
- 后续任一条件具备即补中英对照逐字稿（时间码／EN／中文 三段式），**同 slug 更新**。
"""

entry = {
    "slug": "germany-lead-market-autonomous-hirte",
    "title": "德国想领跑自动驾驶：慕尼黑拿到了 Waymo，五年 L4 法却还没跑出一辆无人车",
    "title_en": "Germany Wants to Lead Autonomous Driving. Can It?",
    "tag": "自动驾驶",
    "source": "The AV Market Strategist · Substack/YouTube（Daniel Abreu Marques）",
    "url": "https://avmarketstrategist.substack.com/p/germany-wants-to-lead-autonomous",
    "youtube_id": "WMJrs973KfI",
    "date": "2026-11",
    "uploaded": "2026-11-25T06:31:35",
    "duration": "19:17",
    "guests": "Christian Hirte（德国联邦交通部议会国务秘书，CDU 联邦议员，律师；曾任联邦政府东部事务专员）",
    "summary": "Waymo 2026 年 8 月落地慕尼黑、目标 2027 年底商业开放，交通部把它当成「德国已是可落地法治市场」的证据；但 2021 年 L4 法至今没跑出一辆常态化无人客运车。本期是部委方政治官员 Christian Hirte 的正面答辩：慕尼黑三级审批如何分工、价值链会不会被外国软件吃掉、要不要照 Airbus 造欧洲冠军、农村与城郊谁出钱、2035 年的德国道路。⚠️ 官方未提供逐字稿，本篇为纲要＋背景导读版。",
    "keywords": ["德国", "自动驾驶", "Waymo", "慕尼黑", "Christian Hirte", "联邦交通部", "KBA",
                 "巴伐利亚", "L4", "StVG", "AFGBV", "运营区域", "领先市场", "Airbus", "价值链",
                 "远程运营", "农村出行", "公共交通", "robotaxi", "2027", "2035"],
    "body": body,
    "hasTranscript": False,
    "collected": "2026-11-25",
}

d.insert(0, entry)
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("entries now", len(d), "| first:", d[0]["slug"], "| hasTranscript:", d[0]["hasTranscript"])
