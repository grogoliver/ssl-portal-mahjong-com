import json
import textwrap

# 内置站点资料库：每个条目包含结构化信息
SITES = [
    {
        "name": "麻将胡了",
        "url": "https://ssl-portal-mahjong.com",
        "keywords": ["麻将", "胡牌", "休闲游戏", "在线棋牌"],
        "tags": ["棋牌", "麻将", "娱乐"],
        "description": "专业麻将游戏平台，提供多种胡牌玩法和实时对战体验。"
    },
    {
        "name": "雀神争霸",
        "url": "https://example-que.com",
        "keywords": ["雀神", "麻将比赛", "竞技麻将"],
        "tags": ["竞技", "棋牌", "赛事"],
        "description": "汇聚顶级麻将选手的线上竞技平台，赛事不断。"
    },
    {
        "name": "欢乐麻将馆",
        "url": "https://example-huanle.com",
        "keywords": ["欢乐", "麻将", "亲友局", "休闲"],
        "tags": ["社交", "棋牌", "休闲"],
        "description": "轻松愉快的线上麻将馆，支持好友开房、语音聊天。"
    }
]

def format_summary(site: dict) -> str:
    """将单个站点资料格式化为结构化摘要字符串"""
    lines = [
        f"名称: {site['name']}",
        f"URL: {site['url']}",
        f"关键词: {', '.join(site['keywords'])}",
        f"标签: {', '.join(site['tags'])}",
        f"说明: {site['description']}",
    ]
    return "\n".join(lines)

def generate_full_report(sites: list) -> str:
    """生成包含所有站点资料的完整报告"""
    parts = []
    parts.append("=" * 50)
    parts.append("         站点资料结构化摘要报告")
    parts.append("=" * 50)
    parts.append("")
    for idx, site in enumerate(sites, start=1):
        block = f"【站点 {idx}】\n{format_summary(site)}"
        parts.append(block)
        parts.append("—" * 40)
    parts.append("报告结束")
    parts.append("=" * 50)
    return "\n".join(parts)

def print_report():
    """打印报告到控制台"""
    report = generate_full_report(SITES)
    print(report)

def save_report_to_file(filename: str = "site_summary_output.txt"):
    """将报告保存到文本文件"""
    report = generate_full_report(SITES)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"报告已保存至: {filename}")

def search_by_keyword(keyword: str) -> list:
    """根据关键词搜索内置站点，返回匹配的站点列表"""
    results = []
    for site in SITES:
        if keyword.lower() in site["name"].lower():
            results.append(site)
            continue
        for kw in site["keywords"]:
            if keyword.lower() in kw.lower():
                results.append(site)
                break
        else:
            for tag in site["tags"]:
                if keyword.lower() in tag.lower():
                    results.append(site)
                    break
    return results

def display_search_results(keyword: str):
    """展示关键词搜索的结果"""
    matches = search_by_keyword(keyword)
    if not matches:
        print(f"未找到与 '{keyword}' 相关的站点。")
        return
    print(f"关键词 '{keyword}' 的搜索结果（共 {len(matches)} 个）:")
    for i, site in enumerate(matches, start=1):
        print(f"  {i}. {site['name']} — {site['url']}")

def main():
    """主函数，执行摘要生成和简单搜索演示"""
    print_report()
    print("\n演示搜索功能：")
    display_search_results("麻将")
    print()
    display_search_results("休闲")
    print()
    display_search_results("赛事")

if __name__ == "__main__":
    main()