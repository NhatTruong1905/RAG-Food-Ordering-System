# TÀI LIỆU TOÀN THƯ HỆ THỐNG ẨM THỰC & ĐẶT MÓN ĂN (FOOD ORDERING KNOWLEDGE BASE)

*Kho tri thức chuẩn hóa dành cho hệ thống RAG (Retrieval-Augmented Generation) tra cứu thực đơn, nhà hàng, món ăn, khẩu vị và chính sách đặt món.*

---

## PHẦN I: TỔNG QUAN HỆ THỐNG VÀ CÁC DANH MỤC ẨM THỰC CHỦ ĐẠO

Hệ thống ẩm thực Food Ordering quy tụ 20 nhà hàng hàng đầu tại TP. Hồ Chí Minh với dải món ăn đa dạng từ ẩm thực truyền thống Việt Nam, ẩm thực Nhật Bản cao cấp, món nướng than hoa Yakiniku, ẩm thực Ý chuẩn vị, món Hoa Dimsum, ẩm thực chay thanh đạm đến món Thái chua cay đặc trưng.

### Danh Sách 10 Danh Mục Ẩm Thực Chuẩn Hóa:
- **Mã danh mục #1**: `Món Khai Vị & Salad`
- **Mã danh mục #2**: `Món Chính Đặc Sắc`
- **Mã danh mục #3**: `Pizza & Mì Ý`
- **Mã danh mục #4**: `Sushi & Sashimi`
- **Mã danh mục #5**: `Dimsum & Món Hoa`
- **Mã danh mục #6**: `Món Chay & Healthy`
- **Mã danh mục #7**: `Món Nướng Yakiniku`
- **Mã danh mục #8**: `Món Việt Truyền Thống`
- **Mã danh mục #9**: `Món Thái Chua Cay`
- **Mã danh mục #10**: `Đồ Uống & Tráng Miệng`

---

## PHẦN II: DANH BẠ VÀ HỒ SƠ 20 NHÀ HÀNG CHI TIẾT (RESTAURANT PROFILES)

### Nhà Hàng #1: Food Shoppe Deli & Market
- **Địa chỉ**: 12 Lê Lợi, Phường Bến Nghé, Quận 1, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7798, Kinh độ 106.699
- **Điểm đánh giá trung bình**: 5 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Thực phẩm Deli tươi ngon, thịt nguội cao cấp, sandwiches hảo hạng và các món phong cách Âu truyền thống.

#### Thực Đơn Món Ăn Phục Vụ Tại Food Shoppe Deli & Market:
##### • Smoked Salmon Caesar Salad (Mã món: #1)
  - **Danh mục**: Món Khai Vị & Salad (Mã #1)
  - **Giá niêm yết**: 125.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: ít béo, thanh mát, cá hồi, phô mai
  - **Mô tả chế biến & thành phần**: Salad cá hồi xông khói Na Uy sốt Caesar truyền thống, bánh mì nướng bơ tỏi giòn rụm và phô mai Parmesan.
##### • Classic Pastrami Reuben Sandwich (Mã món: #2)
  - **Danh mục**: Món Chính Đặc Sắc (Mã #2)
  - **Giá niêm yết**: 165.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: đậm đà, thịt bò, béo ngậy, cay nhẹ
  - **Mô tả chế biến & thành phần**: Bánh mì kẹp thịt bò muối Pastrami nướng giòn kèm phô mai Thụy Sĩ chảy, dưa cải chua New York.
##### • Truffle Roast Beef Panini (Mã món: #3)
  - **Danh mục**: Món Chính Đặc Sắc (Mã #2)
  - **Giá niêm yết**: 185.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: bò nướng, nấm truffle, bánh mì
  - **Mô tả chế biến & thành phần**: Bánh Panini nướng bơ kẹp thịt bò nướng tảng sốt dầu nấm Truffle quý tộc.
##### • New York Baked Cheesecake (Mã món: #4)
  - **Danh mục**: Đồ Uống & Tráng Miệng (Mã #10)
  - **Giá niêm yết**: 75.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: bánh ngọt, phô mai, dâu tây
  - **Mô tả chế biến & thành phần**: Bánh phô mai nướng kiểu New York béo ngậy sốt dâu rừng chua ngọt.

#### Nhận Xét Thực Tế Từ Thực Khách:
- ⭐ 5/5 sao cho món **Smoked Salmon Caesar Salad**: "ngon" (Độ hài lòng: 1)
- ⭐ 5/5 sao cho món **Classic Pastrami Reuben Sandwich**: "tuyệt vời đó hehe" (Độ hài lòng: 1)
- ⭐ 5/5 sao cho món **Truffle Roast Beef Panini**: "Bánh panini giòn tan rất ngon!" (Độ hài lòng: 1)

---

### Nhà Hàng #2: Green Garden Healthy Bistro
- **Địa chỉ**: 45 Trương Định, Phường 6, Quận 3, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7835, Kinh độ 106.691
- **Điểm đánh giá trung bình**: 4.6 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Chuyên các món ăn dinh dưỡng, thực đơn thuần chay, nguyên liệu organic hữu cơ chuẩn quốc tế trong không gian xanh mát.

#### Thực Đơn Món Ăn Phục Vụ Tại Green Garden Healthy Bistro:
##### • Buddha Bowl Hạt Quinoa Bơ Sáp (Mã món: #5)
  - **Danh mục**: Món Chay & Healthy (Mã #6)
  - **Giá niêm yết**: 115.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: ăn chay, hạt quinoa, bơ sáp, healthy
  - **Mô tả chế biến & thành phần**: Tô dinh dưỡng hạt Quinoa cầu vồng, bơ sáp Đắk Lắk, đậu gà hữu cơ và sốt mè rang béo ngậy.
##### • Gỏi Cuốn Nấm Ngũ Sắc Sốt Bơ Đậu Phộng (Mã món: #6)
  - **Danh mục**: Món Chay & Healthy (Mã #6)
  - **Giá niêm yết**: 85.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: thanh đạm, ít béo, rau củ
  - **Mô tả chế biến & thành phần**: Bánh tráng gạo lứt cuộn nấm đùi gà áp chảo, rau mầm tươi mát chấm sốt bơ đậu phộng béo bùi.
##### • Sinh Tố Xanh Detox Cải Kale & Táo (Mã món: #7)
  - **Danh mục**: Đồ Uống & Tráng Miệng (Mã #10)
  - **Giá niêm yết**: 65.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: detox, cải kale, sinh tố healthy
  - **Mô tả chế biến & thành phần**: Cải xoăn Kale hữu cơ xay tươi cùng táo xanh New Zealand và hạt chia thanh lọc cơ thể.

---

### Nhà Hàng #3: Pizza 4P's Bến Thành
- **Địa chỉ**: 8 Thủ Khoa Huân, Phường Bến Thành, Quận 1, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7735, Kinh độ 106.698
- **Điểm đánh giá trung bình**: 4.9 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Pizza nướng lò củi thủ công chuẩn vị Ý kết hợp phô mai tươi tự sản xuất tại Đà Lạt và ẩm thực Nhật Bản tinh tế.

#### Thực Đơn Món Ăn Phục Vụ Tại Pizza 4P's Bến Thành:
##### • Pizza 4 Loại Phô Mai Kèm Mật Ong (Mã món: #8)
  - **Danh mục**: Pizza & Mì Ý (Mã #3)
  - **Giá niêm yết**: 280.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: phô mai béo ngậy, ngọt dịu, nướng củi
  - **Mô tả chế biến & thành phần**: Pizza 4 Cheese trứ danh với phô mai Camembert, Mozzarella, Gorgonzola tự sản xuất rưới mật ong thơm lừng.
##### • Pizza Burrata Thịt Nguội Parma Ham (Mã món: #9)
  - **Danh mục**: Pizza & Mì Ý (Mã #3)
  - **Giá niêm yết**: 320.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: burrata tươi, thịt nguội ý, đẳng cấp
  - **Mô tả chế biến & thành phần**: Phô mai tươi Burrata béo dẻo nguyên quả đặt trên nền thịt nguội Parma Ham Ý muối 24 tháng.
##### • Mì Ý Sốt Kem Cà Chua Thịt Cua Tươi (Mã món: #10)
  - **Danh mục**: Pizza & Mì Ý (Mã #3)
  - **Giá niêm yết**: 245.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: mì ý, thịt cua tươi, sốt kem
  - **Mô tả chế biến & thành phần**: Spaghetti sợi dẻo sốt kem cà chua béo ngậy ngập tràn thịt cua biển tươi tách vỏ trong ngày.

#### Nhận Xét Thực Tế Từ Thực Khách:
- ⭐ 5/5 sao cho món **Pizza 4 Loại Phô Mai Kèm Mật Ong**: "Pizza 4 phô mai ăn cùng mật ong cực kỳ xuất sắc, vỏ bánh thơm mùi củi!" (Độ hài lòng: 0.98)

---

### Nhà Hàng #4: Cơm Niêu Sài Gòn
- **Địa chỉ**: 27 Tú Xương, Phường Võ Thị Sáu, Quận 3, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7821, Kinh độ 106.687
- **Điểm đánh giá trung bình**: 4.7 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Tinh hoa ẩm thực Việt Nam với màn trình diễn cơm đập giòn rụm, cá bống kho tộ và các món đồng quê dân dã đậm đà.

#### Thực Đơn Món Ăn Phục Vụ Tại Cơm Niêu Sài Gòn:
##### • Cơm Đập Niêu Đất Giòn Rụm (Mã món: #11)
  - **Danh mục**: Món Việt Truyền Thống (Mã #8)
  - **Giá niêm yết**: 45.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: cơm cháy giòn, mỡ hành, truyền thống
  - **Mô tả chế biến & thành phần**: Niêu đất đập vỡ trình diễn lấy lớp cơm cháy vàng giòn rưới mỡ hành thơm nức mũi.
##### • Cá Bống Trứng Kho Tộ Tiêu Xanh (Mã món: #12)
  - **Danh mục**: Món Việt Truyền Thống (Mã #8)
  - **Giá niêm yết**: 165.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: đậm đà, cá kho tộ, cay nhẹ
  - **Mô tả chế biến & thành phần**: Cá bống tươi đầy trứng kho keo nước dừa trong tộ đất cùng ớt hiểm và tiêu xanh cay nồng.
##### • Sườn Non Heo Nướng Mật Ong Rừng (Mã món: #13)
  - **Danh mục**: Món Việt Truyền Thống (Mã #8)
  - **Giá niêm yết**: 175.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: sườn nướng, mật ong rừng, cơm niêu
  - **Mô tả chế biến & thành phần**: Sườn non heo ướp mật ong rừng nguyên chất nướng than hoa vàng ruộm thơm lừng.

---

### Nhà Hàng #5: Sushi Hokkaido Sachi
- **Địa chỉ**: 139 Nguyễn Trãi, Phường Bến Thành, Quận 1, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7709, Kinh độ 106.692
- **Điểm đánh giá trung bình**: 4.8 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Hải sản tươi sống nhập khẩu trực tiếp từ vùng biển Hokkaido Nhật Bản cùng nghệ thuật Sashimi và Sushi đỉnh cao.

#### Thực Đơn Món Ăn Phục Vụ Tại Sushi Hokkaido Sachi:
##### • Sashimi Tuyệt Phẩm Hokkaido 5 Loại (Mã món: #14)
  - **Danh mục**: Sushi & Sashimi (Mã #4)
  - **Giá niêm yết**: 495.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: tươi sống, ngọt tự nhiên, hải sản
  - **Mô tả chế biến & thành phần**: Sashimi cá hồi tươi Na Uy, sò điệp Hotate, cá ngừ Akami, bạch tuộc và trứng cá hồi ngâm tương.
##### • Salmon Aburi Cheese Roll (Cuộn Cá Hồi Khò) (Mã món: #15)
  - **Danh mục**: Sushi & Sashimi (Mã #4)
  - **Giá niêm yết**: 185.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: cá hồi khò lửa, phô mai, sushi
  - **Mô tả chế biến & thành phần**: Cơm cuộn cá hồi Na Uy khò lửa thơm lừng sốt kem phô mai chảy béo ngậy và trứng cá chuồn.
##### • Nigiri Bò Wagyu A5 Khò Sốt Ponzu (Mã món: #16)
  - **Danh mục**: Sushi & Sashimi (Mã #4)
  - **Giá niêm yết**: 210.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: bò wagyu a5, nigiri sushi
  - **Mô tả chế biến & thành phần**: Thịt bò Wagyu A5 Nhật Bản vân mỡ cẩm thạch khò tái đặt trên cơm sushi dẻo thơm.

---

### Nhà Hàng #6: Dim Tu Tac Restaurant
- **Địa chỉ**: 55 Đông Du, Phường Bến Nghé, Quận 1, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7761, Kinh độ 106.704
- **Điểm đánh giá trung bình**: 4.7 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Ẩm thực Quảng Đông đương đại với hơn 100 món Dimsum thủ công nóng hổi và vịt quay Bắc Kinh da giòn thượng hạng.

#### Thực Đơn Món Ăn Phục Vụ Tại Dim Tu Tac Restaurant:
##### • Há Cảo Tôm Tươi Thủy Tinh (4 viên) (Mã món: #17)
  - **Danh mục**: Dimsum & Món Hoa (Mã #5)
  - **Giá niêm yết**: 88.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: dimsum, tôm tươi, ngọt thanh
  - **Mô tả chế biến & thành phần**: Vỏ bánh trong suốt thấy rõ nhân tôm sú tươi giòn sần sật hấp nóng trong xửng tre.
##### • Vịt Quay Bắc Kinh Da Giòn Thượng Hạng (Mã món: #18)
  - **Danh mục**: Dimsum & Món Hoa (Mã #5)
  - **Giá niêm yết**: 480.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: vịt quay da giòn, sốt tương ngọt, quảng đông
  - **Mô tả chế biến & thành phần**: Vịt quay da nâu cánh gián giòn rụm cuốn bánh tráng kèm dưa leo, đầu hành và sốt tương ngọt.
##### • Bánh Bao Kim Sa Trứng Muối Tan Chảy (Mã món: #19)
  - **Danh mục**: Dimsum & Món Hoa (Mã #5)
  - **Giá niêm yết**: 68.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: bánh bao kim sa, trứng muối, dimsum
  - **Mô tả chế biến & thành phần**: Bánh bao hấp nóng hổi nhân sốt bơ trứng muối thơm ngậy sánh mịn tan chảy khi bẻ đôi.

---

### Nhà Hàng #7: The Deck Saigon
- **Địa chỉ**: 38 Nguyễn Ư Dĩ, Phường Thảo Điền, TP. Thủ Đức, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.8064, Kinh độ 106.737
- **Điểm đánh giá trung bình**: 4.8 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Nhà hàng ven sông Sài Gòn sang trọng bậc nhất phục vụ ẩm thực Pan-Asian hiện đại và cocktail hoàng hôn lãng mạn.

#### Thực Đơn Món Ăn Phục Vụ Tại The Deck Saigon:
##### • Cua Lột Chiên Giòn Sốt Chanh Dây (Mã món: #20)
  - **Danh mục**: Món Chính Đặc Sắc (Mã #2)
  - **Giá niêm yết**: 260.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: cua lột chiên giòn, sốt chanh dây
  - **Mô tả chế biến & thành phần**: Cua lột nguyên con tẩm bột chiên phồng giòn tan rưới sốt bơ chanh dây chua dịu.
##### • Cá Chẽm Áp Chảo Sốt Bơ Thảo Mộc (Mã món: #21)
  - **Danh mục**: Món Chính Đặc Sắc (Mã #2)
  - **Giá niêm yết**: 340.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: cá chẽm áp chảo, bơ thảo mộc, ven sông
  - **Mô tả chế biến & thành phần**: Phi lê cá chẽm tươi áp chảo da giòn rụm, thịt cá ngọt mềm sốt bơ tỏi thì là.

---

### Nhà Hàng #8: El Gaucho Argentinian Steakhouse
- **Địa chỉ**: 74 Hai Bà Trưng, Phường Bến Nghé, Quận 1, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7782, Kinh độ 106.703
- **Điểm đánh giá trung bình**: 4.9 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Bò bít tết hảo hạng nướng than hoa phong cách Argentina nguyên bản cùng bộ sưu tập rượu vang quốc tế danh tiếng.

#### Thực Đơn Món Ăn Phục Vụ Tại El Gaucho Argentinian Steakhouse:
##### • Black Angus Ribeye Steak 250g (Mã món: #22)
  - **Danh mục**: Món Chính Đặc Sắc (Mã #2)
  - **Giá niêm yết**: 790.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: thịt bò hảo hạng, thơm khói than hoa, đậm đà
  - **Mô tả chế biến & thành phần**: Thăn bò Black Angus nướng than hoa Medium Rare kèm sốt tiêu đen Chimichurri kiểu Argentina.
##### • Wagyu Filet Mignon 200g (Mã món: #23)
  - **Danh mục**: Món Chính Đặc Sắc (Mã #2)
  - **Giá niêm yết**: 1.250.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: bò wagyu, bít tết thượng hạng
  - **Mô tả chế biến & thành phần**: Thịt bò Wagyu vân mỡ tuyệt hảo nướng mềm mọng như bơ tan trong miệng.

---

### Nhà Hàng #9: Hum Vegetarian Lounge & Restaurant
- **Địa chỉ**: 32 Võ Văn Tần, Phường Võ Thị Sáu, Quận 3, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7779, Kinh độ 106.691
- **Điểm đánh giá trung bình**: 4.9 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Không gian ẩm thực chay thanh tịnh, sáng tạo kết hợp thảo mộc thiên nhiên và các món ăn giàu dinh dưỡng cho sức khỏe.

#### Thực Đơn Món Ăn Phục Vụ Tại Hum Vegetarian Lounge & Restaurant:
##### • Cơm Chiên Gạo Lứt Hạt Sen Lá Sen (Mã món: #24)
  - **Danh mục**: Món Chay & Healthy (Mã #6)
  - **Giá niêm yết**: 135.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: ăn chay, thanh đạm, ít dầu mỡ, nhiều chất xơ
  - **Mô tả chế biến & thành phần**: Gạo lứt thơm dẻo xào cùng hạt sen Huế, nấm đông cô tươi bọc trong lá sen hấp thanh khiết.
##### • Gỏi Nấm Tràm Thảo Mộc Chua Ngọt (Mã món: #25)
  - **Danh mục**: Món Chay & Healthy (Mã #6)
  - **Giá niêm yết**: 120.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: gỏi nấm, thảo mộc, chua ngọt
  - **Mô tả chế biến & thành phần**: Nấm tràm Phú Quốc dai giòn bóp gỏi rau răm, hoa chuối và đậu phộng rang.

---

### Nhà Hàng #10: Phở Thìn Lò Đúc - Chi Nhánh Sài Gòn
- **Địa chỉ**: 110 Hai Bà Trưng, Phường Đa Kao, Quận 1, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7845, Kinh độ 106.699
- **Điểm đánh giá trung bình**: 4.5 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Thương hiệu phở bò tái lăn trứ danh Hà Nội với nước dùng béo ngậy, ngập tràn hành lá tươi và thịt bò xào lửa lớn thơm nức.

#### Thực Đơn Món Ăn Phục Vụ Tại Phở Thìn Lò Đúc - Chi Nhánh Sài Gòn:
##### • Phở Bò Tái Lăn Đặc Biệt Ngập Hành (Mã món: #26)
  - **Danh mục**: Món Việt Truyền Thống (Mã #8)
  - **Giá niêm yết**: 90.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: phở tái lăn, hành hoa, nước béo đậm đà
  - **Mô tả chế biến & thành phần**: Bát phở bò tái lăn trứ danh xào lửa lớn thơm mùi khói, nước dùng ngọt tủy đậm đà ngập tràn hành hoa.
##### • Quẩy Giòn Hà Nội (Đĩa 3 chiếc) (Mã món: #27)
  - **Danh mục**: Món Việt Truyền Thống (Mã #8)
  - **Giá niêm yết**: 15.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: quẩy giòn, ăn kèm phở
  - **Mô tả chế biến & thành phần**: Quẩy chiên vàng ruộm giòn tan chấm nước dùng phở bò nóng hổi.

---

### Nhà Hàng #11: Secret Garden Home-cooked Vietnamese
- **Địa chỉ**: 158 Pasteur, Phường Bến Nghé, Quận 1, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7789, Kinh độ 106.698
- **Điểm đánh giá trung bình**: 4.6 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Quán ăn sân thượng đậm chất thôn quê Việt Nam mộc mạc giữa lòng phố thị với các món cơm nhà gia đình thân thuộc.

#### Thực Đơn Món Ăn Phục Vụ Tại Secret Garden Home-cooked Vietnamese:
##### • Thịt Ba Rọi Kho Trứng Cút Nước Dừa (Mã món: #28)
  - **Danh mục**: Món Việt Truyền Thống (Mã #8)
  - **Giá niêm yết**: 135.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: thịt kho tàu, nước dừa, cơm nhà
  - **Mô tả chế biến & thành phần**: Thịt ba rọi mềm rục béo ngậy kho cùng trứng cút trong nước dừa xiêm Bến Tre ngả màu cánh gián.

---

### Nhà Hàng #12: Bếp Mẹ Ỉn - Authentic Vietnamese Street Food
- **Địa chỉ**: 136 Lê Thánh Tôn, Phường Bến Thành, Quận 1, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.773, Kinh độ 106.698
- **Điểm đánh giá trung bình**: 4.7 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Đạt giải thưởng Michelin Bib Gourmand với món bánh xèo tôm nhảy giòn rụm, cơm chiên trái dừa và gà nướng ống tre.

#### Thực Đơn Món Ăn Phục Vụ Tại Bếp Mẹ Ỉn - Authentic Vietnamese Street Food:
##### • Bánh Xèo Tôm Nhảy Vỏ Giòn Michelin (Mã món: #29)
  - **Danh mục**: Món Việt Truyền Thống (Mã #8)
  - **Giá niêm yết**: 110.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: bánh xèo giòn, tôm nhảy, michelin
  - **Mô tả chế biến & thành phần**: Bánh xèo miền Tây tôm sông tươi nhảy tanh tách, vỏ mỏng giòn rụm cuốn rau rừng bánh tráng.

---

### Nhà Hàng #13: Gyu-Shige Yakiniku Ngưu Phồn
- **Địa chỉ**: 119 Hồ Tùng Mậu, Phường Bến Nghé, Quận 1, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7731, Kinh độ 106.704
- **Điểm đánh giá trung bình**: 4.6 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Thương hiệu nướng than hoa Yakiniku Nhật Bản với các phần thịt bò Wagyu, dẻ sườn ướp sốt Miso đặc quyền hảo vị.

#### Thực Đơn Món Ăn Phục Vụ Tại Gyu-Shige Yakiniku Ngưu Phồn:
##### • Dẻ Sườn Bò Mỹ Ướp Sốt Miso Đặc Quyền (Mã món: #30)
  - **Danh mục**: Món Nướng Yakiniku (Mã #7)
  - **Giá niêm yết**: 230.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: bò nướng yakiniku, sốt miso, thịt nướng than
  - **Mô tả chế biến & thành phần**: Dẻ sườn bò Mỹ đan xen vân mỡ nướng than hoa Yakiniku chín vàng mọng nước chấm sốt tương Nhật.

---

### Nhà Hàng #14: Pasta Fresca Thảo Điền
- **Địa chỉ**: 28 Thảo Điền, Phường Thảo Điền, TP. Thủ Đức, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.8034, Kinh độ 106.732
- **Điểm đánh giá trung bình**: 4.7 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Mì Ý tươi sợi thủ công cán trong ngày kết hợp cùng sốt Pesto béo thơm, sốt bò bằm Bolognese và phô mai Burrata tươi ngậy.

#### Thực Đơn Món Ăn Phục Vụ Tại Pasta Fresca Thảo Điền:
##### • Mì Ý Tagliatelle Tươi Sốt Bolognese (Mã món: #31)
  - **Danh mục**: Pizza & Mì Ý (Mã #3)
  - **Giá niêm yết**: 195.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: mì ý tươi, sốt bolognese bò bằm
  - **Mô tả chế biến & thành phần**: Sợi mì tươi cán thủ công trong ngày hòa quyện sốt thịt bò bằm Bolognese nấu chậm 4 tiếng.

---

### Nhà Hàng #15: Chay Garden Vegetarian Restaurant & Coffee
- **Địa chỉ**: 52 Võ Văn Tần, Phường Võ Thị Sáu, Quận 3, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7765, Kinh độ 106.69
- **Điểm đánh giá trung bình**: 4.8 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Biệt thự cổ phong cách Đông Dương lãng mạn phục vụ các món chay thuần khiết, trà sen hữu cơ và đồ tráng miệng thanh mát.

#### Thực Đơn Món Ăn Phục Vụ Tại Chay Garden Vegetarian Restaurant & Coffee:
##### • Đậu Hũ Non Sốt Trái Lựu Chua Ngọt (Mã món: #32)
  - **Danh mục**: Món Chay & Healthy (Mã #6)
  - **Giá niêm yết**: 105.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: đậu hũ non, sốt lựu, món chay đông dương
  - **Mô tả chế biến & thành phần**: Đậu hũ non chiên giòn áo lớp sốt nước ép quả lựu đỏ tự nhiên thanh tao giải nhiệt.

---

### Nhà Hàng #16: San Fu Lou Cantonese Kitchen
- **Địa chỉ**: 76A Lê Lai, Phường Bến Thành, Quận 1, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7709, Kinh độ 106.695
- **Điểm đánh giá trung bình**: 4.6 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Bếp mở chuẩn phong cách Hong Kong với mì kéo tươi truyền thống, há cảo sò điệp bó xôi và vịt quay thơm lừng.

#### Thực Đơn Món Ăn Phục Vụ Tại San Fu Lou Cantonese Kitchen:
##### • Mì Kéo Tay Xá Xíu Quảng Đông Sốt Dầu Hào (Mã món: #33)
  - **Danh mục**: Dimsum & Món Hoa (Mã #5)
  - **Giá niêm yết**: 125.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: mì kéo tươi, xá xíu mật ong, hongkong
  - **Mô tả chế biến & thành phần**: Mì trứng kéo tay thủ công dai mềm ăn kèm thịt xá xíu mật ong nướng thơm phức.

---

### Nhà Hàng #17: Tokyo Deli Sushi
- **Địa chỉ**: 240 Phan Xích Long, Phường 2, Quận Phú Nhuận, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7963, Kinh độ 106.689
- **Điểm đánh giá trung bình**: 4.4 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Chuỗi ẩm thực Nhật Bản quen thuộc với thực đơn đa dạng từ Sushi, Sashimi, Set Lunch Bento văn phòng đến lẩu ấm cúng.

#### Thực Đơn Món Ăn Phục Vụ Tại Tokyo Deli Sushi:
##### • Set Bento Cá Hồi Sốt Teriyaki (Mã món: #34)
  - **Danh mục**: Sushi & Sashimi (Mã #4)
  - **Giá niêm yết**: 135.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: bento cá hồi, sốt teriyaki, nhật bản
  - **Mô tả chế biến & thành phần**: Cơm Bento dinh dưỡng gồm cá hồi Na Uy áp chảo sốt Teriyaki, trứng cuộn, salad mè và canh miso.

---

### Nhà Hàng #18: Marukame Udon
- **Địa chỉ**: 215 Lý Tự Trọng, Phường Bến Thành, Quận 1, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7722, Kinh độ 106.695
- **Điểm đánh giá trung bình**: 4.5 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Mì Udon tươi truyền thống vùng Sanuki Nhật Bản luộc tươi trực tiếp trước mặt khách cùng quầy Tempura vàng rụm tự chọn.

#### Thực Đơn Món Ăn Phục Vụ Tại Marukame Udon:
##### • Mì Udon Bò Kake Nước Dùng Dashi (Mã món: #35)
  - **Danh mục**: Món Chính Đặc Sắc (Mã #2)
  - **Giá niêm yết**: 89.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: mì udon sanuki, thịt bò, dashi nhật
  - **Mô tả chế biến & thành phần**: Sợi mì Udon tươi dày dẻo Sanuki trứ danh ngập trong nước dùng Dashi thanh ngọt kèm thịt bò thái lát mềm.
##### • Tempura Tôm Sú Khổng Lồ Chiên Giòn (Mã món: #36)
  - **Danh mục**: Món Khai Vị & Salad (Mã #1)
  - **Giá niêm yết**: 35.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: tempura tôm giòn rụm
  - **Mô tả chế biến & thành phần**: Tôm sú tươi tẩm bột xù Tempura chiên vàng rụm chấm nước tương gừng củ cải.

---

### Nhà Hàng #19: Quán Bụi - Vietnamese Bistro
- **Địa chỉ**: 19 Ngô Văn Năm, Phường Bến Nghé, Quận 1, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7812, Kinh độ 106.705
- **Điểm đánh giá trung bình**: 4.7 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Ẩm thực ba miền Việt Nam chuẩn vị gia đình không bột ngọt, phong cách Đông Dương hoài cổ và ấm áp.

#### Thực Đơn Món Ăn Phục Vụ Tại Quán Bụi - Vietnamese Bistro:
##### • Chả Giò Quán Bụi Hải Sản Đặc Biệt (Mã món: #37)
  - **Danh mục**: Món Việt Truyền Thống (Mã #8)
  - **Giá niêm yết**: 125.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: chả giò hải sản, giòn tan
  - **Mô tả chế biến & thành phần**: Chả giò tôm cua thịt cuốn bánh tráng rế chiên giòn tan chấm nước mắm chua ngọt chuẩn vị.

---

### Nhà Hàng #20: TukTuk Thai Bistro
- **Địa chỉ**: 38 Lý Tự Trọng, Phường Bến Nghé, Quận 1, TP.HCM
- **Tọa độ vị trí**: Vĩ độ 10.7774, Kinh độ 106.702
- **Điểm đánh giá trung bình**: 4.6 / 5.0 ⭐
- **Mô tả & Phong cách ẩm thực**: Ẩm thực đường phố Thái Lan biến tấu phong cách hiện đại với súp Tomyum chua cay, gỏi đu đủ Somtum và xôi xoài ngọt ngào.

#### Thực Đơn Món Ăn Phục Vụ Tại TukTuk Thai Bistro:
##### • Súp Tomyum Hải Sản Nước Cốt Dừa (Mã món: #38)
  - **Danh mục**: Món Thái Chua Cay (Mã #9)
  - **Giá niêm yết**: 175.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: súp tomyum, chua cay, cốt dừa béo
  - **Mô tả chế biến & thành phần**: Súp tôm sú, mực tươi nấu cùng củ riềng, lá chúc, sả cây và nước cốt dừa chua cay chuẩn vị Bangkok.
##### • Xôi Xoài Nước Cốt Dừa Thái Lan (Mã món: #39)
  - **Danh mục**: Đồ Uống & Tráng Miệng (Mã #10)
  - **Giá niêm yết**: 85.000 VNĐ
  - **Hương vị đặc trưng (Flavor Tags)**: xôi xoài, nước cốt dừa, món thái
  - **Mô tả chế biến & thành phần**: Xôi nếp dẻo thơm rưới nước cốt dừa mặn ngọt ăn kèm xoài chín vàng ngọt lịm.

---

## PHẦN III: CẨM NANG HƯỚNG DẪN CHỌN MÓN THEO KHẨU VỊ & SỞ THÍCH (TASTE & DIETARY GUIDE)

### 1. Dành Cho Người Ăn Chay, Thực Dưỡng & Ăn Sạch (Vegetarian & Healthy):
- **Green Garden Healthy Bistro** (45 Trương Định, Q.3): Nổi bật với `Buddha Bowl Hạt Quinoa Bơ Sáp` (115.000 VNĐ), `Gỏi Cuốn Nấm Ngũ Sắc Sốt Bơ Đậu Phộng` (85.000 VNĐ), và `Sinh Tố Xanh Detox Cải Kale & Táo` (65.000 VNĐ).
- **Hum Vegetarian Lounge & Restaurant** (32 Võ Văn Tần, Q.3): Đẳng cấp không gian thanh tịnh, món ăn nổi tiếng gồm `Cơm Chiên Gạo Lứt Hạt Sen Lá Sen` (135.000 VNĐ) và `Gỏi Nấm Tràm Thảo Mộc Chua Ngọt` (120.000 VNĐ).
- **Chay Garden Vegetarian Restaurant & Coffee** (52 Võ Văn Tần, Q.3): Biệt thự Đông Dương với món `Đậu Hũ Non Sốt Trái Lựu Chua Ngọt` (105.000 VNĐ).


### 2. Dành Cho Tín Đồ Thịt Bò Hảo Hạng, BBQ & Nướng Than Hoa:
- **El Gaucho Argentinian Steakhouse** (74 Hai Bà Trưng, Q.1): Trải nghiệm bít tết đẳng cấp thế giới với `Black Angus Ribeye Steak 250g` (790.000 VNĐ) và `Wagyu Filet Mignon 200g` (1.250.000 VNĐ) nướng mềm mọng như bơ.
- **Gyu-Shige Yakiniku Ngưu Phồn** (119 Hồ Tùng Mậu, Q.1): Nổi tiếng với `Dẻ Sườn Bò Mỹ Ướp Sốt Miso Đặc Quyền` (230.000 VNĐ) nướng than hoa Yakiniku mọng nước.
- **Food Shoppe Deli & Market** (12 Lê Lợi, Q.1): Sandwiches thịt bò cao cấp với `Classic Pastrami Reuben Sandwich` (165.000 VNĐ) và `Truffle Roast Beef Panini` (185.000 VNĐ).


### 3. Dành Cho Tín Đồ Hải Sản Tươi Sống, Sushi & Món Nhật:
- **Sushi Hokkaido Sachi** (139 Nguyễn Trãi, Q.1): Đỉnh cao với `Sashimi Tuyệt Phẩm Hokkaido 5 Loại` (495.000 VNĐ - cá hồi Na Uy, sò điệp Hotate, cá ngừ Akami, bạch tuộc, trứng cá hồi), `Salmon Aburi Cheese Roll` (185.000 VNĐ), và `Nigiri Bò Wagyu A5 Khò Sốt Ponzu` (210.000 VNĐ).
- **Tokyo Deli Sushi** (240 Phan Xích Long, Phú Nhuận): Set ăn tiện lợi như `Set Bento Cá Hồi Sốt Teriyaki` (135.000 VNĐ).
- **Marukame Udon** (215 Lý Tự Trọng, Q.1): Mì Udon tươi Sanuki `Mì Udon Bò Kake Nước Dùng Dashi` (89.000 VNĐ) ăn kèm `Tempura Tôm Sú Khổng Lồ Chiên Giòn` (35.000 VNĐ).


### 4. Dành Cho Người Yêu Ẩm Thực Việt Nam Truyền Thống & Dân Dã:
- **Cơm Niêu Sài Gòn** (27 Tú Xương, Q.3): Trình diễn `Cơm Đập Niêu Đất Giòn Rụm` (45.000 VNĐ) ăn cùng `Cá Bống Trứng Kho Tộ Tiêu Xanh` (165.000 VNĐ) và `Sườn Non Heo Nướng Mật Ong Rừng` (175.000 VNĐ).
- **Bếp Mẹ Ỉn** (136 Lê Thánh Tôn, Q.1 - Michelin Bib Gourmand): Nổi tiếng với `Bánh Xèo Tôm Nhảy Vỏ Giòn Michelin` (110.000 VNĐ).
- **Phở Thìn Lò Đúc Sài Gòn** (110 Hai Bà Trưng, Q.1): Bát `Phở Bò Tái Lăn Đặc Biệt Ngập Hành` (90.000 VNĐ) xào khói thơm nức cùng `Quẩy Giòn Hà Nội` (15.000 VNĐ).
- **Secret Garden** (158 Pasteur, Q.1): Cơm nhà truyền thống với `Thịt Ba Rọi Kho Trứng Cút Nước Dừa` (135.000 VNĐ).
- **Quán Bụi - Vietnamese Bistro** (19 Ngô Văn Năm, Q.1): `Chả Giò Quán Bụi Hải Sản Đặc Biệt` (125.000 VNĐ).


### 5. Dành Cho Tín Đồ Pizza & Pasta Chuẩn Ý:
- **Pizza 4P's Bến Thành** (8 Thủ Khoa Huân, Q.1): Nổi tiếng lừng danh với `Pizza 4 Loại Phô Mai Kèm Mật Ong` (280.000 VNĐ) làm từ phô mai tươi Camembert, Mozzarella, Gorgonzola tự sản xuất; `Pizza Burrata Thịt Nguội Parma Ham` (320.000 VNĐ); và `Mì Ý Sốt Kem Cà Chua Thịt Cua Tươi` (245.000 VNĐ).
- **Pasta Fresca Thảo Điền** (28 Thảo Điền, TP. Thủ Đức): Mì thủ công `Mì Ý Tagliatelle Tươi Sốt Bolognese` (195.000 VNĐ) sốt bò bằm nấu chậm 4 tiếng.


### 6. Dành Cho Người Thích Dimsum & Ẩm Thực Quảng Đông:
- **Dim Tu Tac Restaurant** (55 Đông Du, Q.1): `Há Cảo Tôm Tươi Thủy Tinh` (88.000 VNĐ), `Vịt Quay Bắc Kinh Da Giòn Thượng Hạng` (480.000 VNĐ), và `Bánh Bao Kim Sa Trứng Muối Tan Chảy` (68.000 VNĐ).
- **San Fu Lou Cantonese Kitchen** (76A Lê Lai, Q.1): `Mì Kéo Tay Xá Xíu Quảng Đông Sốt Dầu Hào` (125.000 VNĐ).


### 7. Dành Cho Người Thích Món Thái Chua Cay:
- **TukTuk Thai Bistro** (38 Lý Tự Trọng, Q.1): `Súp Tomyum Hải Sản Nước Cốt Dừa` (175.000 VNĐ) chua cay chuẩn vị Bangkok và `Xôi Xoài Nước Cốt Dừa Thái Lan` (85.000 VNĐ).

---

## PHẦN IV: HỒ SƠ KHÁCH HÀNG & MẪU ĐẶT HÀNG THỰC TẾ

### Khách Hàng: customer_an (Mã #2)
- **Địa chỉ mặc định**: 123 Nguyễn Huệ, Phường Bến Nghé, Quận 1, TP.HCM
- **Khẩu vị & Sở thích ẩm thực**: cay, đậm đà, thích thịt bò, pizza, steak


### Khách Hàng: customer_binh (Mã #3)
- **Địa chỉ mặc định**: 45 Trương Định, Phường 6, Quận 3, TP.HCM
- **Khẩu vị & Sở thích ẩm thực**: ăn chay, thanh đạm, ít dầu mỡ, nhiều rau, organic


### Khách Hàng: customer_chi (Mã #4)
- **Địa chỉ mặc định**: 78 Nam Kỳ Khởi Nghĩa, Phường 7, Quận 3, TP.HCM
- **Khẩu vị & Sở thích ẩm thực**: sushi, hải sản tươi sống, dimsum, món thái


---

## PHẦN V: QUY TRÌNH ĐẶT HÀNG, THANH TOÁN & VẬN HÀNH

### 1. Phương Thức Thanh Toán Hỗ Trợ:
- **CASH (Tiền mặt)**: Thanh toán trực tiếp khi nhận hàng (COD).
- **CREDIT_CARD (Thẻ tín dụng / Ghi nợ quốc tế)**: Visa, Mastercard, JCB.
- **E_WALLET (Ví điện tử MoMo, ZaloPay)**: Quét mã QR tiện lợi.
- **VNPAY (Cổng thanh toán quốc gia VNPay)**: Thanh toán an toàn qua Mobile Banking.


### 2. Các Trạng Thái Đơn Hàng (Order Statuses):
- `PENDING`: Đơn hàng vừa được khởi tạo, đang chờ xác nhận thanh toán/nhà hàng duyệt.
- `CONFIRMED`: Nhà hàng đã nhận đơn và xác nhận chế biến.
- `PREPARING`: Bếp đang thực hiện nấu nướng và đóng gói món ăn.
- `DELIVERING`: Tài xế giao nhận đang trên đường vận chuyển tới địa chỉ khách hàng.
- `COMPLETED`: Khách hàng đã nhận món thành công.
- `CANCELLED`: Đơn hàng bị hủy do khách hàng hoặc nhà hàng hết món.


### 3. Vận Chuyển & Phủ Sóng:
- Phạm vi giao hàng trải rộng khắp TP. Hồ Chí Minh: Quận 1, Quận 3, Phú Nhuận, Thảo Điền (TP. Thủ Đức).
- Thời gian chế biến và giao hàng trung bình từ 25 - 45 phút tùy theo cự ly và trạng thái nhà hàng.