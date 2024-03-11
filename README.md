# Bước 1
* Mở file tmp.xlsx 
![image](https://github.com/TienMinhHoa/bo-Linkedin/assets/114821401/b9549593-050d-4cc8-b2d8-5777e65cf85f)
* Cột content điền nội dung bài đăng
* Cột Tag điền tên người muốn tag, khi muốn tag nhiều người thì điền cách tên người cách nhau 1 dấu xuống dòng(Xuống dòng trong Excel nhấn alt+Enter)
* Cột Hashtag điền hashtag, khi muốn có nhiều hastag thì điền cách nhau 1 dấu xuống dòng
* Cột image là cột ảnh đính kèm. Điền đường link tuyệt đối dẫn đến file ảnh trong máy(bỏ trống nếu k muốn có ảnh).
* Mỗi 1 dòng(ID) trong file tương ứng với 1 bài đăng.


# Bước 2
* Sau khi đã chỉnh sửa được file xlsx, ta vào thư mục dist/bot_linkedin/bot_linkedin.exe
* Đợi 1 lát, cửa sổ đăng nhập vào linkedin hiện lên, ta sẽ tiến hành đăng nhập.
* Sau khi đăng nhập, sau 3 giây, sẽ hiện 1 cửa sổ như thế này:
![image](https://github.com/TienMinhHoa/bo-Linkedin/assets/114821401/4aa9ce36-e47e-45d0-80e5-28826bf57c45)
* Starting Row là dòng đầu tiên của list bài cần đăng
* Ending Row là dòng cuối cùng list bài cần đăng(chú ý không được để trống 2 mục này)
* Sau khi nhập xong 2 mục, bấm **run**, bot sẽ lấy thông tin trong file xlsx theo quy ước như trên để bắt đầu đăng bài.



