---
name: membership-renewal-support
description: Use this skill when a user asks about renewal rules, how to cancel auto-renew, cannot find the cancel entry, says auto-renew cancellation failed, or says they canceled but were still charged. Do not use it for refund or complaint requests, benefit-not-arrived issues, or unrelated app feature problems. The skill queries membership status with a Python script, explains auto-renew rules, and routes the case through bundled references for renewal consultation or cancellation troubleshooting.
---

# Membership Renewal Support

用于处理会员续费规则咨询、取消续费引导、以及“无法关闭自动续费/关闭失败”类问题。

## 使用条件

命中以下任一情况时使用：

- 用户咨询续费规则
- 用户咨询如何取消续费
- 用户反馈无法取消自动续费
- 用户反馈取消自动续费失败
- 用户称已关闭自动续费，但仍被扣款

## 何时不使用

出现以下情况时不要使用本 skill，应转对应场景：

- 用户明确提出“退款 / 退钱 / 投诉”等交易售后诉求
- 用户反馈已成功扣款，但会员时长或权益未到账
- 用户只咨询会员权益区别
- 用户反馈播放、下载等其他 App 功能异常

## 资源导航

- 会员信息查询脚本：`scripts/query_membership.py`
- 自动扣费规则与关闭入口：`references/auto-renew-rules.md`
- 续费咨询分流：`references/renewal-consultation-routing.md`
- 取消续费失败分流：`references/auto-renew-cancellation-routing.md`
- 支付渠道与特殊设备指引：`references/payment-channel-guides.md`

## 字段映射

脚本返回字段与业务字段的对应关系：

- `vipstatus` = `{账号_会员信息_新系统_当前会员状态}`
- `renewstatus` = `{账号_会员信息_新系统_续费状态}`
- `accountstatus` = `{账号_会员信息_新系统_账号状态}`
- `starttime` / `endtime` = 会员起止时间

常用的补充字段来自上游系统，不能臆造：

- `{账号_自动续费通知_是否发送}`
- `{账号_会员_历史订阅信息}`
- `{账号_会员_昵称_同设备}`
- 最近一笔成功订单的 `paid_time`

## 执行流程

1. 先识别用户意图：

- 规则咨询、为什么会续费、未收到通知、扣款日与展示日不一致、支付方式变化、延迟扣费：读 `references/renewal-consultation-routing.md`
- 找不到关闭入口、关闭失败、已关闭仍扣款、换设备/注销/封禁后无法关闭：读 `references/auto-renew-cancellation-routing.md`
- 如涉及具体关闭路径或 Apple 特殊问题，同时读 `references/payment-channel-guides.md`

2. 先执行会员查询脚本：

```bash
python3 scripts/query_membership.py <user_id>
```

3. 结合脚本结果和上游字段做判断：

- 先看 `renewstatus`
- 再看 `vipstatus`
- 涉及“仍被扣款”时，再核对解约时间、扣款时间、同设备账号
- 涉及“未收到通知”时，再查通知发送记录

4. 输出时遵循：

- 规则解释优先使用 `auto-renew-rules.md`
- 分流判断优先使用对应 `*-routing.md`
- 关闭路径和设备/Apple 例外优先使用 `payment-channel-guides.md`
- 对用户不可见的内部判断，只用于内部流转，不直接向用户暴露

## 处理原则

- 明确区分“自动续费规则咨询”和“退款投诉”
- 无法代用户关闭支付渠道自动扣款，要解释安全原因并继续给出路径
- 需要补证据时，只索取必要信息，如扣款截图、时间、渠道、金额
- 若原始资料写有“内部客服可见，用户不可见”，对外回复时不要直接照搬内部描述
