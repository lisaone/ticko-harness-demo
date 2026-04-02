# 自动扣费规则与关闭入口

## 1. 自动扣费规则

为保证会员权益不中断，系统会在当前计费周期结束前，按照支付渠道规则自动尝试扣费。

### 1.1 支付宝、抖音支付

- 扣费时间：通常在下一个计费周期开始前 24 小时自动扣费
- 关闭路径：
  - 支付宝 App > 我的 > 设置 > 支付设置 > 免密支付/自动扣款
  - 抖音 App > 我 > 右上角菜单 > 我的钱包 > 设置 > 自动扣款/免密支付

### 1.2 微信支付

- 扣费时间：通常在下一个计费周期开始前 48 小时自动扣费
- 关闭路径：
  - 微信 App > 我 > 服务 > 钱包 > 支付设置 > 自动续费

### 1.3 Apple 订阅（App Store）

- 扣费时间：通常在计费周期结束前 24 小时内扣费，具体以苹果系统实际处理时间为准
- 关闭路径：
  - iOS 12 及以上：App Store > 右上角头像 > 订阅
  - iOS 12 以下：设置 > iTunes Store 与 App Store > 查看 Apple ID > 订阅

## 2. App 内关闭自动续费入口

### 2.1 直达关闭按钮

关闭续费按钮：

`hybrid://lynxview/?dynamic=1&surl=https%3A%2F%2Flf-sourcecdn-tos.bytegecko.com%2Fobj%2Fbyte-gurd-source%2F10899%2Fgecko%2Fresource%2Fvip%2Ftemplate.js&bdhm_bid=luna_vip_center&bdhm_pid=vip&loader_name=forest&channel=vip&bundle=template.js&autoRenew=1&show_nav_bar=0`

### 2.2 App 内通用入口

- 汽水音乐 App > 我的 > 会员中心 > 套餐续费信息
- 若页面中未看到“套餐续费信息”或“下期会员将于……”等提示，通常说明当前登录账号未开通自动续费

### 2.3 缓存提示

- 用户完成关闭操作后，页面状态可能存在短暂延迟
- 建议用户重启 App 后重新进入会员中心确认是否显示“已关闭”
