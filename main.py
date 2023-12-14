from uuid import UUID, uuid4
from typing import List
from fastapi import FastAPI, HTTPException

from models import Gender, Role, UpdateUser, User

app = FastAPI()

db: List[News] = [
    News(title:"En Son Teknoloji Haberleri",description: "Yeni nesil yapay zeka teknolojileri hakkında güncel bilgiler.",imageUrl: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Sağlıklı Yaşam İpuçları",description: "Düzenli egzersiz ve sağlıklı beslenmeyle ilgili pratik öneriler.",imageUrl: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Moda Dünyasında Son Trendler", description:"Mevsimin en popüler giyim ve aksesuar modası.",imageUrl: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Bilimde Yeni Keşifler",description: "Güneş sistemi dışında yeni bir gezegenin keşfi.",imageUrl: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Finans Haberleri ve Analiz",description: "Piyasa güncellemeleri ve ekonomik analizler.",imageUrl: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Seyahat Rehberi: Roma",description: "Roma'da gezilecek yerler ve yerel lezzetler.",imageUrl: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Film İncelemesi: 'Yitik Şehir'",description: "Yeni çıkan filmin detaylı bir incelemesi.",imageUrl: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Spor Gündemi: Futbol Transferleri",description: "Futbol dünyasındaki en son transfer haberleri.",imageUrl: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Yemek Tarifi: Avokado Salatası",description: "Sağlıklı ve lezzetli avokado salatasının tarifi.",imageUrl: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Teknoloji İncelemesi: Akıllı Telefon XYZ",description: "Yeni çıkan akıllı telefonun detaylı incelemesi.",imageUrl: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Doğa Fotoğrafçılığı: Renkli Sonbahar",description: "Sonbaharda doğanın muhteşem renk paleti.", "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Sağlık Bilgisi: Yoga ve Stres Yönetimi",description: "Yoga pratiğinin stresle başa çıkma üzerindeki etkileri.",imageUrl: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Oyun İncelemesi: 'Fantastik Macera'",description: "Yeni çıkan video oyununun detaylı incelemesi.",imageUrl: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Eğitim Haberleri: Uzaktan Eğitim Yenilikleri",description: "Dijital eğitimde en son gelişmeler ve yenilikler.",imageUrl: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    News(title:"Sanat Galerisi: Modern Sanat Sergisi",description: "Güncel sanat eserlerinin sergilendiği etkinlik.",coverImg: "https://images.pexels.com/photos/159652/table-food-book-newspaper-159652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"),
    


]


@app.get("/api/v1/getNews")
async def fetch_GetNews():
    return db


@app.get("/")
async def root():
    return {"Hello": "World"}


# @app.get("/api/v1/users/{user_id}")
# async def fetch_user(user_id: UUID):
#     user = next((user for user in db if user.id == user_id), None)
#     return user


# @app.post("/api/v1/users")
# async def register_user(user: User):
#     db.append(user)
#     return {"id": user.id}


# @app.delete("/api/v1/users/{user_id}")
# async def delete_user(user_id: UUID):
#     user = next((user for user in db if user.id == user_id), None)
#     if user:
#         db.remove(user)
#         return {"message": f"{user.id} User deleted successfully"}
#     raise HTTPException(
#         status_code=404, detail=f"User with id:{user_id} does not exist"
#     )


# @app.put("/api/v1/users/{user_id}")
# async def update_user(update_user: UpdateUser, user_id: UUID):
#     for user in db:
#         if user.id == user_id:
#             if update_user.first_name is not None:
#                 user.first_name = update_user.first_name
#             if update_user.last_name is not None:
#                 user.last_name = update_user.last_name
#             if update_user.middle_name is not None:
#                 user.middle_name = update_user.middle_name
#             if update_user.roles is not None:
#                 user.roles = update_user.roles
#             if update_user.gender is not None:
#                 user.gender = update_user.gender

#             return {"message": f"{user.id} User updated successfully"}
#     raise HTTPException(
#         status_code=404, detail=f"User with id:{user_id} does not exist"
#     )
