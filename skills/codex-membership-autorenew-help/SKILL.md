---
name: membership_autorenew_help
title: 汽水音乐会员自动续费咨询与关闭指引
description: 处理会员自动续费规则咨询、取消续费路径说明、无法关闭自动续费等问题；不处理退款、到账异常、会员权益差异咨询。
---

# 汽水音乐会员自动续费咨询与关闭指引

本 skill 用于处理“自动续费规则咨询”和“无法关闭自动续费”两类问题。`SKILL.md` 只保留触发条件、执行步骤和文件导航；详细规则、话术与冲突修正放在 `references/`。

## 何时使用

满足以下任一情况时使用：

- 用户咨询续费规则、自动扣费原因
- 用户咨询如何关闭自动续费
- 用户反馈找不到关闭入口、取消失败
- 用户声称已经关闭，但仍被扣款
- 用户反馈未收到续费通知
- 用户咨询扣款时间、展示续费时间、支付方式变化、延迟扣费等与自动续费相关的问题

## 何时不使用

出现以下情况时，不使用本 skill，直接转对应场景：

- 用户明确提出“退款 / 退钱 / 投诉 / 赔偿”等交易售后诉求
- 用户反馈扣款成功但会员时长或权益未到账
- 用户仅咨询会员权益区别
- 用户反馈播放、下载等非续费问题

## 资源导航

- 范围、字段、总原则：`references/scope-fields-and-principles.md`
- 自动扣费规则与关闭入口：`references/auto-renew-rules.md`
- 自动续费与扣费咨询分流：`references/renewal-consultation-routing.md`
- 无法关闭自动续费分流：`references/auto-renew-cancellation-routing.md`
- 回复风格与冲突修正：`references/writing-and-conflicts.md`
- 会员查询脚本：`scripts/query_membership.py`

## 执行流程

1. 先读 `references/scope-fields-and-principles.md`，确认是否在 skill 适用范围内。
2. 若不适用，停止本 skill，并提示转入退款、到账异常或其他对应场景。
3. 若适用，执行：

```bash
python3 scripts/query_membership.py <user_id>
```

4. 结合脚本结果和上游字段补查信息，按用户核心意图分流：

- “为什么会自动续费 / 未收到通知 / 提前扣费 / 支付方式变化 / 延迟补扣”等，读 `references/renewal-consultation-routing.md`
- “找不到关闭入口 / 取消失败 / 已关闭仍被扣款 / 换设备无法关闭”等，读 `references/auto-renew-cancellation-routing.md`
- 解释扣费规则、关闭路径时，同时读 `references/auto-renew-rules.md`

5. 输出回复前，再核对 `references/writing-and-conflicts.md`：

- 避免暴露内部字段和内部策略
- 异常场景不要误用“正常续费”话术
- 需要用户操作时，明确说明平台无法代操作的原因是账户与支付安全

## 脚本字段映射

- `vipstatus` = `{账号_会员信息_新系统_当前会员状态}`
- `renewstatus` = `{账号_会员信息_新系统_续费状态}`
- `accountstatus` = `{账号_会员信息_新系统_账号状态}`
- `starttime` / `endtime` = 会员起止时间

## 使用提醒

- 对用户不可见的内部说明，只用于判断和流转，不直接对外复述
- 若用户表达同时涉及两个子场景，优先回答最强诉求，再补充另一类指引
