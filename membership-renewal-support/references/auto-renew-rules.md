# 自动扣费规则与关闭入口

## 自动扣费规则

为确保用户的会员权益不中断，平台会针对不同支付渠道在不同时间周期内进行自动扣费。

### 支付渠道 1：支付宝、抖音支付

- 自动扣费时间：每个计费周期开始前 24 小时
- 关闭自动续费路径：
  - 支付宝：支付宝 App → 我的 → 设置 → 支付设置 → 免密支付/自动扣款
  - 抖音支付：抖音 App → 我 → 右上角菜单 → 我的钱包 → 设置 → 自动扣款/免密支付

### 支付渠道 2：微信支付

- 自动扣费时间：每个计费周期开始前 48 小时
- 关闭自动续费路径：
  - 微信：微信 App → 我 → 服务 → 钱包 → 支付设置 → 自动续费

### 支付渠道 3：Apple 订阅

- 自动扣费时间：通常在计费周期结束前 24 小时内，具体以苹果系统处理为准
- 关闭自动续费路径：
  - iOS 12 及以上：App Store → 右上角头像 → 订阅
  - iOS 12 以下：设置 → iTunes Store 与 App Store → 查看 Apple ID → 订阅

## 自动续费关闭入口

### 1. 直达按钮

- 关闭续费按钮：
  `hybrid://lynxview/?dynamic=1&surl=https%3A%2F%2Flf-sourcecdn-tos.bytegecko.com%2Fobj%2Fbyte-gurd-source%2F10899%2Fgecko%2Fresource%2Fvip%2Ftemplate.js&bdhm_bid=luna_vip_center&bdhm_pid=vip&loader_name=forest&channel=vip&bundle=template.js&autoRenew=1&show_nav_bar=0`

### 2. App 内通用入口

- 汽水音乐 App → 我的 → 会员中心 → 套餐续费信息 → 按页面提示关闭

补充说明：

- 如果未看到“套餐续费信息”或“下期会员将于...”字样，通常表示当前登录账号未开通自动续费
- 关闭成功后，如页面未即时刷新，建议重启 App 后再次查看续费状态是否更新为“已关闭”

### 3. 支付渠道 App 内管理

- 用户也可以直接在签约的支付渠道 App 内管理自动续费
- 详细路径见 `payment-channel-guides.md`
