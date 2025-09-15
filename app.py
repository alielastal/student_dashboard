import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# إعداد العنوان
st.title("📊 لوحة تحكم أداء الطلاب")

# تحميل البيانات
@st.cache
def load_data():
    return pd.read_csv("students.csv")

df = load_data()

# عرض البيانات
st.subheader("📋 بيانات الطلاب")
st.dataframe(df)

# إحصائيات عامة
st.subheader("📈 إحصائيات عامة")
col1, col2, col3 = st.columns(3)
col1.metric("متوسط الحضور", f"{df['attendance_percent'].mean():.1f}%")
col2.metric("متوسط ساعات الدراسة", f"{df['hours_studied'].mean():.1f}")
col3.metric("متوسط نتيجة الامتحان", f"{df['exam_score'].mean():.1f}")

# رسم بياني: ساعات الدراسة مقابل نتيجة الامتحان
st.subheader("🎓 العلاقة بين ساعات الدراسة ودرجة الامتحان")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="hours_studied", y="exam_score", hue="attendance_percent", palette="viridis", ax=ax)
st.pyplot(fig)

# فلترة الطلاب حسب الحضور
st.subheader("🔍 تصفية الطلاب حسب نسبة الحضور")
attendance_threshold = st.slider("أدخل الحد الأدنى للحضور", 0, 100, 50)
filtered_df = df[df["attendance_percent"] >= attendance_threshold]
st.write(f"عرض {filtered_df.shape[0]} طالباً/طالبة لديهم حضور ≥ {attendance_threshold}%")
st.dataframe(filtered_df)
