"""Beginner data analyst project: compute KPIs from retail sales CSV."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "sales_data.csv"
REPORT_PATH = Path(__file__).resolve().parents[1] / "reports" / "summary_report.md"


def parse_number(value: str) -> float:
    """Convert numeric text to float with safe default."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def load_rows(path: Path) -> list[dict[str, str]]:
    """Load CSV rows."""
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def calculate_metrics(rows: list[dict[str, str]]) -> dict[str, object]:
    """Calculate core KPIs and grouped revenue summaries."""
    total_revenue = 0.0
    category_revenue = defaultdict(float)
    city_revenue = defaultdict(float)
    channel_revenue = defaultdict(float)
    product_revenue = defaultdict(float)

    for row in rows:
        units = parse_number(row.get("units_sold", "0"))
        price = parse_number(row.get("unit_price", "0"))
        discount = parse_number(row.get("discount_pct", "0")) / 100
        net_revenue = units * price * (1 - discount)

        total_revenue += net_revenue
        category_revenue[row.get("category", "Unknown")] += net_revenue
        city_revenue[row.get("city", "Unknown")] += net_revenue
        channel_revenue[row.get("channel", "Unknown")] += net_revenue
        product_revenue[row.get("product", "Unknown")] += net_revenue

    order_count = len(rows)
    average_order_value = total_revenue / order_count if order_count else 0.0

    top_categories = sorted(category_revenue.items(), key=lambda x: x[1], reverse=True)
    top_cities = sorted(city_revenue.items(), key=lambda x: x[1], reverse=True)
    top_products = sorted(product_revenue.items(), key=lambda x: x[1], reverse=True)[:5]

    return {
        "order_count": order_count,
        "total_revenue": total_revenue,
        "average_order_value": average_order_value,
        "top_categories": top_categories,
        "top_cities": top_cities,
        "channel_revenue": dict(channel_revenue),
        "top_products": top_products,
    }


def format_currency(value: float) -> str:
    return f"₹{value:,.2f}"


def write_report(metrics: dict[str, object], output_path: Path) -> None:
    """Write a markdown summary report."""
    lines = [
        "# Retail Sales KPI Summary",
        "",
        "## Overall Performance",
        f"- Total Orders: **{metrics['order_count']}**",
        f"- Total Revenue: **{format_currency(metrics['total_revenue'])}**",
        f"- Average Order Value: **{format_currency(metrics['average_order_value'])}**",
        "",
        "## Revenue by Category",
    ]

    for category, revenue in metrics["top_categories"]:
        lines.append(f"- {category}: **{format_currency(revenue)}**")

    lines.extend(["", "## Revenue by City"])
    for city, revenue in metrics["top_cities"]:
        lines.append(f"- {city}: **{format_currency(revenue)}**")

    lines.extend(["", "## Revenue by Channel"])
    for channel, revenue in sorted(metrics["channel_revenue"].items()):
        lines.append(f"- {channel}: **{format_currency(revenue)}**")

    lines.extend(["", "## Top 5 Products by Revenue"])
    for product, revenue in metrics["top_products"]:
        lines.append(f"- {product}: **{format_currency(revenue)}**")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    rows = load_rows(DATA_PATH)
    metrics = calculate_metrics(rows)
    write_report(metrics, REPORT_PATH)
    print(f"Analysis complete. Report saved to: {REPORT_PATH}")


if __name__ == "__main__":
    main()
