# main.py
from fastmcp import FastMCP
import requests
from constant import API_HOST, API_PORT

BASE_URL = f"http://{API_HOST}:{API_PORT}"

mcp = FastMCP(name="KPI Analysis Agent")

@mcp.tool(name="get_kpi_summary", description="Get KPI summary stats")
def tool_kpi_summary():
    resp = requests.get(f"{BASE_URL}/kpi/summary")
    return resp.json()

@mcp.tool(name="get_kpi_trend", description="Get trend data for a KPI")
def tool_kpi_trend(kpi_name: str):
    resp = requests.get(f"{BASE_URL}/kpi/trend/{kpi_name}")
    return resp.json()

@mcp.tool(name="analyze_kpi", description="High-level KPI analysis")
def tool_analyze_kpi():
    resp = requests.get(f"{BASE_URL}/kpi/summary")
    summary = resp.json()
    analysis = []
    for kpi, stats in summary.items():
        if kpi == "sales" and stats["mean"] < 100:
            analysis.append(f"{kpi} 销售额偏低，需要营销提升。平均值：{stats['mean']}")
        elif kpi == "conversion_rate" and stats["mean"] < 0.05:
            analysis.append(f"{kpi} 转化率偏低，需要优化转化策略。平均值：{stats['mean']}")
        else:
            analysis.append(f"{kpi} 表现良好。平均值：{stats['mean']}")
    return analysis

if __name__ == "__main__":
    mcp.run()