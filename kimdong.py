import streamlit as st
import pandas as pd
from streamlit import session_state as state
import warnings
warnings.filterwarnings('ignore')
import re
from datetime import datetime
import base64
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load dữ liệu từ các tệp tin CSV
data_truyen_tranh = pd.read_csv("data/Truyện tranh thiếu nhi.csv")
data_khoa_hoc = pd.read_csv("data/Kiến Thức - Khoa Học.csv")
data_manga = pd.read_csv("data/Manga_Comic.csv")
data_VietNam = pd.read_csv("data/Văn học Việt Nam.csv")
data_nuoc_ngoai = pd.read_csv("data/Văn học nước ngoài.csv")

st.markdown("""
    <style>
        .sidebar .sidebar-content {
            width: 200px;
        }
        .main {
            width: calc(100% - 180px);
        }
    </style>
""", unsafe_allow_html=True)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode("utf-8")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{encoded_image}');
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        }}
        .stApp > div {{
            background-color: rgba(255, 255, 255, 0.8);
            padding: 42px;
            border-radius: 0px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("picture/background.jpg")


def show_products(data):
    df_gio_hang = state.df_gio_hang  # Lấy giỏ hàng từ session state

    num_cols = 4  # Số cột hiển thị
    num_products = len(data)
    num_rows = (num_products + num_cols - 1) // num_cols  # Số hàng hiển thị

    for i in range(num_rows):
        columns = st.columns(num_cols)
        for j in range(i * num_cols, min((i + 1) * num_cols, num_products)):
            with columns[j % num_cols]:
                st.image(data.loc[j, 'Link hình ảnh'], use_column_width=True)
                st.write(data.loc[j, 'Tên sách'])
        columns = st.columns(num_cols)
        for j in range(i * num_cols, min((i + 1) * num_cols, num_products)):
            with columns[j % num_cols]:
                gia = data.loc[j, 'Giá']
                st.write('Giá bán:', gia)
                if st.button('Thêm vào giỏ hàng', key=f'add_to_cart_{j}'): 
                    df_gio_hang = pd.concat([df_gio_hang, data.loc[[j], ['Tên sách', 'Giá']]], axis = 0) # Thêm sản phẩm vào giỏ hàng
                    state.df_gio_hang = df_gio_hang  # Lưu giỏ hàng vào session state
                with st.expander('Thông tin...'):
                    st.write("Đã bán: ", data.loc[j, "Đã bán"])
                    st.write("Rating: ", data.loc[j, "Đánh giá"])
                    st.write('**Nội dung:** ', data.loc[j, "Nội dung"])



# Trang giới thiệu
def gioi_thieu_page():
    st.write('## GIỚI THIỆU NHÀ XUẤT BẢN KIM ĐỒNG')  
    st.markdown('''<p style="text-align: justify">Nhà xuất bản Kim Đồng trực thuộc Trung ương Đoàn TNCS Hồ Chí Minh là Nhà xuất bản tổng hợp có chức năng xuất bản sách và văn hóa phẩm phục vụ thiếu nhi và các bậc phụ huynh trong cả nước, quảng bá và giới thiệu văn hóa Việt Nam ra thế giới.
Nhà xuất bản có nhiệm vụ tổ chức bản thảo, biên soạn, biên dịch, xuất bản và phát hành các xuất bản phẩm có nội dung: giáo dục truyền thống dân tộc, giáo dục về tri thức, kiến thức… trên các lĩnh vực văn học, nghệ thuật, khoa học kỹ thuật nhằm cung cấp cho các em thiếu nhi cũng như các bậc phụ huynh các kiến thức cần thiết trong cuộc sống, những tinh hoa của tri thức nhân loại nhằm góp phần giáo dục và hình thành nhân cách thế hệ trẻ.
Đối tượng phục vụ của Nhà xuất bản là các em từ tuổi nhà trẻ mẫu giáo (1 đến 5 tuổi), nhi đồng (6 đến 9 tuổi), thiếu niên (10 đến 15 tuổi) đến các em tuổi mới lớn (16 đến 18 tuổi) và các bậc phụ huynh.</p>''', unsafe_allow_html = True)

    st.write('''
#### THÔNG TIN CHUNG  
Tên giao dịch: Nhà xuất bản Kim Đồng  
Tên giao dịch quốc tế: Kim Dong Publishing House  
Ngày thành lập: 17 tháng 6 năm 1957  
Cơ quan chủ quản: Trung ương Đoàn TNCS Hồ Chí Minh

**Trụ sở chính:**  
Địa chỉ: 55 Quang Trung, Hà Nội, Việt Nam  
Điện thoại: (024) 39434730 – (024)3 9428653  
Fax: (024) 38229085  
Email: info@nxbkimdong.com.vn  
Website: www.nxbkimdong.com.vn  

**Chi nhánh tại TP. Hồ Chí Minh**  
Địa chỉ: 248 Cống Quỳnh, P. Phạm Ngũ Lão, Q.1, TP. Hồ Chí Minh  
Điện thoại: (028) 39303832 – (028) 39303447  
Fax: (028) 39305867  
Email: cnkimdong@nxbkimdong.com.vn  

**Chi nhánh tại Miền Trung**  
Địa chỉ: 102 Ông Ích Khiêm, TP Đà Nẵng, Việt Nam  
Điện thoại: (0511) 3812333 – (0511) 3812335  
Fax: (0511) 3812334  
Email: cnkimdongmt@nxbkimdong.com.vn 
    ''')

# Trang truyện tranh thiếu nhi
def truyen_tranh_page():
    st.write('## Truyện tranh thiếu nhi')
    st.image('picture/thieu_nhi.jpg')
    show_products(data_truyen_tranh)

# Trang kiến thức - khoa học
def khoa_hoc_page():
    st.write('## Kiến Thức - Khoa Học')
    st.image('picture/khoa_hoc.jpg')
    show_products(data_khoa_hoc)

# Trang manga_comic
def manga_comic_page():
    st.write('## Manga_Comic')
    st.image('picture/manga.jpg')
    show_products(data_manga)

# Trang văn học Việt Nam
def vietnam_page():
    st.write('## Văn học Việt Nam')
    st.image('picture/vietnam.jpg')
    show_products(data_VietNam)

# Trang văn học nước ngoài
def nuoc_ngoai_page():
    st.write('## Văn học nước ngoài')
    st.image('picture/nuoc_ngoai.jpg')
    show_products(data_nuoc_ngoai)


# Trang giỏ hàng
def gio_hang_page():
    df_gio_hang = state.df_gio_hang  # Lấy giỏ hàng từ session state

    st.write('## Giỏ hàng')
    # st.dataframe(df_gio_hang)
    # Hiển thị bảng sản phẩm
    df_gio_hang.reset_index(drop=True, inplace=True)
    for i, row in df_gio_hang.iterrows():
        quantity = st.number_input(f"**{row['Tên sách']} - Giá: {row['Giá']} đồng**", value=1, min_value=0, max_value=100, step=1, key=i)
        df_gio_hang.loc[i, 'Số lượng'] = quantity
        df_gio_hang.loc[i, 'Thành tiền'] = quantity * row['Giá']

    tong = df_gio_hang['Thành tiền'].sum()
    st.write(f'### Tổng tiền: {tong:,.0f} đồng')
    # Kiểm tra xem người dùng đã nhập thông tin đầy đủ hay chưa
    is_info_complete = False
    st.write('Vui lòng cung cấp thông tin dưới đây.')
    ho_ten = st.text_input('Họ và tên:')
    dia_chi = st.text_input('Địa chỉ:')
    sdt = st.text_input('Số điện thoại:')
    pattern = r'^(0[2-9]|84[2-9]|\+84[2-9])\d{8}$'
    if st.button('THANH TOÁN'):
        if ho_ten != '' and dia_chi != '' and sdt != '':
            if re.match(pattern, sdt):
                is_info_complete = True
            else:
                st.error("Số điện thoại không hợp lệ. Vui lòng cung cấp chính xác số điện thoại của bạn để chúng tôi có thể giao hàng đến bạn.")

    if is_info_complete:
        st.success('Đặt hàng thành công!')
        st.write('Chúng tôi sẽ giao hàng cho bạn trong vòng 3-5 ngày làm việc.')
        tdiem = datetime.now().strftime('%Y%m%d%H%M%S')
        df_gio_hang.to_csv(f'orders/{ho_ten}_{dia_chi}_{sdt}_{tdiem}.csv')


# Trang thong_ke
def thong_ke_page():
    st.write('## Thống kê')
    data_khoa_hoc['Thể loại'] = 'Kiến Thức - Khoa Học'
    data_manga['Thể loại'] = 'Manga_Comic'
    data_truyen_tranh['Thể loại'] = 'Truyện tranh thiếu nhi'
    data_nuoc_ngoai['Thể loại'] = 'Văn học nước ngoài'
    data_VietNam['Thể loại'] = 'Văn học Việt Nam'
    df_gop = pd.concat([data_khoa_hoc, data_manga, data_nuoc_ngoai, data_truyen_tranh, data_VietNam], ignore_index=True)
    sns.countplot(data=df_gop, y='Thể loại', order = df_gop['Thể loại'].value_counts().index)
    plt.title('Thống kê số lượng sách - truyện theo Thể loại')
    plt.xlabel('Số sách - truyện')
    st.pyplot()
    
    
    data_df = {
    'Truyện tranh thiếu nhi': data_truyen_tranh,
    'Kiến Thức - Khoa Học': data_khoa_hoc,
    'Manga_Comic': data_manga,
    'Văn học Việt Nam': data_VietNam,
    'Văn học nước ngoài': data_nuoc_ngoai}

    bang = st.selectbox('Bạn muốn xem thông tin thống kê của:', list(data_df.keys()))
    df = data_df[bang]
    st.write('Top 10 sách - truyện được mua nhiều nhất')
    sns.barplot(data = df.sort_values('Đã bán', ascending=False).head(10), x = 'Đã bán', y = 'Tên sách')
    st.pyplot()
    st.write('Phân phối của số lượng sách đã bán')
    sns.boxplot(data = df, y = 'Đã bán')
    st.pyplot()
    st.write('Top 10 sách - truyện được được đánh giá cao nhất')
    sns.barplot(data = df.sort_values('Đánh giá', ascending=False).head(10), x = 'Đánh giá', y = 'Tên sách')
    st.pyplot()
    st.write('Phân phối của rating')
    sns.boxplot(data = df, y = 'Đánh giá')
    st.pyplot()
    st.write('Top 10 sách - truyện có giá bán cao nhất')
    sns.barplot(data = df.sort_values('Giá', ascending=False).head(10), x = 'Giá', y = 'Tên sách')
    st.pyplot()
    st.write('Phân phối giá bán')
    sns.boxplot(data = df, y = 'Giá')
    st.pyplot()
   

    




# Ứng dụng chính
def main():
    if 'df_gio_hang' not in state:
        state.df_gio_hang = pd.DataFrame(columns=['Tên sách', 'Giá', 'Số lượng', 'Thành tiền'])  # Khởi tạo giỏ hàng trong session state
    
    tabs = {
        "Giới thiệu": gioi_thieu_page,
        "Truyện tranh thiếu nhi": truyen_tranh_page,
        "Kiến Thức - Khoa Học": khoa_hoc_page,
        "Manga_Comic": manga_comic_page,
        "Văn học Việt Nam": vietnam_page,
        "Văn học nước ngoài": nuoc_ngoai_page,
        "Giỏ hàng": gio_hang_page,
        "Thống kê": thong_ke_page
    }

    choice = st.sidebar.radio("DANH MỤC", list(tabs.keys()))

    page = tabs[choice]
    page()

main()
