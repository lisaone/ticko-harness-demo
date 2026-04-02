---
name: membership-auto-renew-support
description: Use this skill when a user cannot find the auto-renew cancellation entry, says they already canceled but were still charged, or cannot cancel because of account logout, ban, device change, or Apple subscription limitations. The skill routes the case by membership status and renew status, runs a Python membership query script, and uses bundled references for scenario judgment and channel-specific guidance.
---

# Membership Auto-Renew Support

用于处理“无法关闭自动续费”相关咨询。保持 `SKILL.md` 精简，只在这里说明流程；详细判定规则和话术放在 `references/`，查询逻辑放在 `scripts/`。

## 何时使用

当用户出现以下任一情况时使用本 skill：

- 在 App 内找不到关闭自动续费入口
- 声称已经关闭自动续费，但仍被扣款
- 因账号注销、封禁、换设备、换系统等原因，无法按原路径关闭

## 资源导航

- 会员状态查询脚本：`scripts/query_membership.py`
- 场景判定与标准话术：`references/scenario-routing.md`
- 支付渠道关闭路径与特殊问题引导：`references/channel-guides.md`

## 字段映射

脚本返回字段与业务字段的对应关系：

- `vipstatus` = `{账号_会员信息_新系统_当前会员状态}`
- `renewstatus` = `{账号_会员信息_新系统_续费状态}`
- `accountstatus` = `{账号_会员信息_新系统_账号状态}`
- `starttime` / `endtime` = 会员起止时间

注意：`accountstatus` 不是“当前会员状态”，它表示账号状态。

## 执行流程

1. 先获取用户 ID，并执行：

```bash
python3 scripts/query_membership.py <user_id>
```

2. 读取返回结果，重点看：

- `vipstatus`
- `renewstatus`
- `accountstatus`

3. 若还需以下信息，则从上游系统补充查询，不要臆造：

- `{账号_会员_昵称_同设备}`
- `{账号_会员_历史订阅信息-最近一笔订阅的解约时间}`
- 最近一笔成功订单的 `paid_time`
- 扣款渠道、金额、订单截图

4. 按如下顺序路由：

- `renewstatus = 续费中`：直接去 `references/channel-guides.md`
- `renewstatus in [已解约, "-", ""]`：继续看 `vipstatus`，并参考 `references/scenario-routing.md`
- 用户明确反馈“仍被扣款”时，优先核对扣款时间、解约时间、同设备账号和扣款渠道

## 处理原则

- 正常续费要明确说明“扣款发生时间”和“关闭时间”的先后关系
- 需要用户补充证据时，只索取与判定直接相关的信息，如扣款截图、时间、渠道、金额
- 无法代用户关闭支付渠道自动扣款，需解释安全原因后继续指引
- Apple 订阅问题统一按支付渠道规则处理，不承诺平台侧代操作

## 输出要求

- 优先使用 `references/scenario-routing.md` 中的标准回复模板
- 渠道关闭路径和 Apple 特殊问题，使用 `references/channel-guides.md`
- 若命中异常扣款场景，明确说明需要截图并转产品/财经侧处理
