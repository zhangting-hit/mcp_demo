# helper.py
from constant import KPI_DATA, KPI_LIST
from typing import Dict, List

def get_kpi_summary() -> Dict:
    """返回KPI指标的汇总分析"""
    summary = {}
    for kpi in KPI_LIST:
        values = [day[kpi] for day in KPI_DATA]
        summary[kpi] = {
            "mean": round(sum(values) / len(values), 2),
            "max": max(values),
            "min": min(values)
        }
    return summary

def get_kpi_trend(kpi_name: str) -> List[Dict]:
    """返回某个KPI的时间趋势"""
    if kpi_name not in KPI_LIST:
        return {"error": "Invalid KPI name"}
    return [{"date": day["date"], kpi_name: day[kpi_name]} for day in KPI_DATA]

def analyze_kpi():
    """高层分析"""
    summary = get_kpi_summary()
    analysis = []
    for kpi, stats in summary.items():
        if stats["mean"] < 100 and kpi == "sales":
            analysis.append(f"{kpi} 销售额偏低，需要营销提升。平均值：{stats['mean']}")
        elif kpi == "conversion_rate" and stats["mean"] < 0.05:
            analysis.append(f"{kpi} 转化率偏低，需要优化转化策略。平均值：{stats['mean']}")
        else:
            analysis.append(f"{kpi} 表现良好。平均值：{stats['mean']}")
    return analysis