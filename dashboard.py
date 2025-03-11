import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from flask import Flask

# สร้าง Flask Server
server = Flask(__name__)
app = dash.Dash(__name__, server=server)

# โหลดผลลัพธ์จากการพยากรณ์
file_path = "D:\Term_Project\pm_2.5\predicted_pm25.csv"  # แก้ไขให้เป็นตำแหน่งที่ถูกต้อง
predictions = pd.read_csv(file_path)

# ตรวจสอบชื่อคอลัมน์การทำนาย
prediction_column = [col for col in predictions.columns if "predict" in col.lower()]
if prediction_column:
    prediction_column = prediction_column[0]
else:
    raise ValueError("ไม่พบคอลัมน์การทำนายในไฟล์ CSV")

# แปลง datetime เป็น datetime
predictions["datetime"] = pd.to_datetime(predictions["datetime"])

# สร้างกราฟ Plotly
fig = px.line(predictions, x="datetime", y=prediction_column, title="พยากรณ์ค่า PM 2.5 (7 วันข้างหน้า)",
              labels={"datetime": "เวลา", prediction_column: "PM 2.5"}, markers=True)

# ออกแบบ Layout ของ Dashboard
app.layout = html.Div([
    html.H1("Dashboard การพยากรณ์ค่า PM 2.5"),
    dcc.Graph(figure=fig)
])

# เรียกใช้แอป
if __name__ == "__main__":
    app.run_server(debug=True)
