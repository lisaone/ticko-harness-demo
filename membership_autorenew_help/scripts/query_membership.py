from __future__ import annotations

import argparse
import json
import random
from datetime import datetime, timedelta
from typing import Dict, TypedDict


class MembershipRecord(TypedDict):
    vipstatus: str
    accountstatus: str
    renewstatus: str
    starttime: str
    endtime: str


def query_membership_record(user_id: str) -> MembershipRecord:
    """
    模拟查询会员信息。
    接入真实环境时，应替换为数据库 / RPC / HTTP 调用。
    """
    del user_id

    vipstatus_values = ["svip", "free", "vip", "free_vip"]
    accountstatus_values = ["正常", "异常"]
    renewstatus_values = ["已解约", "续费中"]

    start_dt = datetime.now() - timedelta(
        days=random.randint(1, 365),
        seconds=random.randint(0, 86400),
    )
    end_dt = start_dt + timedelta(
        days=random.randint(1, 365),
        seconds=random.randint(1, 86400),
    )

    return {
        "vipstatus": random.choice(vipstatus_values),
        "accountstatus": random.choice(accountstatus_values),
        "renewstatus": random.choice(renewstatus_values),
        "starttime": start_dt.strftime("%Y-%m-%d %H:%M:%S"),
        "endtime": end_dt.strftime("%Y-%m-%d %H:%M:%S"),
    }


def get_user_membership_status(user_id: str) -> Dict[str, str]:
    """
    输入：用户 ID
    输出：string -> string 的状态字典
    字段映射：
    - vipstatus      -> {账号_会员信息_新系统_当前会员状态}
    - renewstatus    -> {账号_会员信息_新系统_续费状态}
    - accountstatus  -> {账号_会员信息_新系统_账号状态}
    """
    record = query_membership_record(user_id)

    return {
        "vipstatus": record.get("vipstatus", ""),
        "accountstatus": record.get("accountstatus", ""),
        "starttime": record.get("starttime", ""),
        "endtime": record.get("endtime", ""),
        "renewstatus": record.get("renewstatus", ""),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="查询会员基础状态")
    parser.add_argument("user_id", help="用户 ID")
    args = parser.parse_args()

    result = get_user_membership_status(args.user_id)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
