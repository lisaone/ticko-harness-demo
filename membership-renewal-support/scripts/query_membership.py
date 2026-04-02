from __future__ import annotations

import argparse
import json
import random
from datetime import datetime, timedelta
from typing import Dict


def query_membership_record(user_id: str) -> dict:
    """
    模拟查询会员信息。
    接入真实环境时，可以把这里替换为数据库、RPC 或 HTTP 调用。
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
    输入: 用户 ID
    输出: 所有 value 都是 string 的 map 结构
    """
    record = query_membership_record(user_id)

    return {
        "vipstatus": str(record.get("vipstatus", "")),
        "accountstatus": str(record.get("accountstatus", "")),
        "endtime": str(record.get("endtime", "")),
        "starttime": str(record.get("starttime", "")),
        "renewstatus": str(record.get("renewstatus", "")),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Query membership status for a user.")
    parser.add_argument("user_id", help="User ID to query")
    args = parser.parse_args()

    result = get_user_membership_status(args.user_id)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
