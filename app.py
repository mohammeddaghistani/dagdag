import streamlit as st
import pandas as pd
import numpy as np

# --- 1. إعدادات الصفحة الأساسية (يجب أن يكون أول أمر) ---
st.set_page_config(
    page_title="نظام التقييم الإيجاري",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. دالة التنسيق الجمالي (CSS) ---
def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    /* تنسيق الخط والاتجاه */
    html, body, [class*="css"], .stMarkdown, .stText {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* إخفاء القوائم الافتراضية لستريمليت */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}

    /* الهيدر الاحترافي */
    .main-header {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 25px rgba(30, 58, 138, 0.2);
    }

    /* تحسين البطاقات (Metrics) */
    [data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        transition: 0.3s;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.05);
    }

    /* تنسيق الجداول */
    .stDataFrame {
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        overflow: hidden;
    }

    /* تنسيق الأزرار */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background: #1E3A8A;
        color: white;
        font-weight: bold;
        height: 3rem;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #3B82F6;
        color: white;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

local_css()

# --- 3. القائمة الجانبية (Sidebar) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/602/602181.png", width=100) # أيقونة تجريبية
    st.title("لوحة التحكم")
    st.subheader("فلترة البيانات")
    region = st.selectbox("اختر المنطقة", ["الرياض", "جدة", "الدمام", "مكة المكرمة"])
    property_type = st.multiselect("نوع العقار", ["سكني", "تجاري", "إداري"], default="سكني")
    st.divider()
    st.info("هذا النظام مدعوم بالذكاء الاصطناعي لتقدير القيم الإيجارية.")

# --- 4. محتوى الصفحة الرئيسي ---

# الهيدر
st.markdown("""
    <div class="main-header">
        <h1>🏛️ نظام التقييم الإيجاري الذكي</h1>
        <p>نظام متطور لتحليل وتخمين القيم العقارية بناءً على معايير السوق الحالية</p>
    </div>
""", unsafe_allow_html=True)

# صف الإحصائيات (Metrics)
m1, m2, m3, m4 = st.columns(4)
m1.metric("متوسط سعر المتر", "550 ر.س", "12%+")
m2.metric("عدد العقارات", "2,840", "150+")
m3.metric("دقة التقييم", "94%", "0.5%+")
m4.metric("تغير السوق", "مستقر", "تحسن")

st.markdown("### 📊 نظرة عامة على السوق")

# تقسيم الشاشة للرسوم والجداول
left_col, right_col = st.columns([1.2, 1])

with left_col:
    st.subheader("تحليل الاتجاه الزمني")
    # بيانات تجريبية للرسم
    chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['العام الماضي', 'العام الحالي'])
    st.line_chart(chart_data)

with right_col:
    st.subheader("آخر التقييمات المنفذة")
    # بيانات تجريبية للجدول
    df = pd.DataFrame({
        "العقار": ["شقة فاخرة", "محل تجاري", "فيلا دبلكس", "مكتب"],
        "الحي": ["الملقا", "الروضة", "الياسمين", "العليا"],
        "التقييم (ر.س)": ["60,000", "120,000", "180,000", "95,000"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# زر إجراء عملية تقييم جديدة
st.divider()
if st.button("🚀 ابدأ تقييم عقار جديد الآن"):
    st.balloons()
    st.success("تم تفعيل وضع التقييم الذكي!")
