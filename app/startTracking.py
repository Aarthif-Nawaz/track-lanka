from app import db
from app.DB import Tracking,User
from app.Spiders.scrape_spiders import woolsworth,officeWorks
from app.send_email import send_email

def fetchProductsData():
    tracking = Tracking.query.all()
    print(tracking)
    data = []
    for track in tracking:
        product ={
            "id":track.id,
            "name":track.store_name,
            "url":track.product_url,
            "title":track.product_name,
            "set_price":float(track.set_price),
            "current_price":float(track.current_price),
            "user_id":track.user_id
        }
        data.append(product)

    return data

def startTracking():
    products = fetchProductsData()
    for product in products:
        current_track = Tracking.query.filter_by(id=product['id']).first()
        user = User.query.filter_by(id=current_track.user_id).first()
        if(product['name']=="Woolsworth"):
            price = woolsworth(product['url'])
            print(price)
            new_price = price['price'].split("$")
            if(float(new_price[1]) < product['current_price']):
                current_track.current_price = float(new_price[1])
                send_email(user.email,"Congratulations ! Price Has Come Down Low ", f"Hi {user.name} the price has come down for the product {product['name']} from {product['current_price']} to {new_price[1]}.Please Visit Store {product['url']} to buy the product")
            elif(float(new_price[1]) == product['set_price']):
                current_track.current_price = float(new_price[1])
                send_email(user.email,"Congratulations ! Price Has Come Down To Your Desired Price ", f"Hi {user.name} the price has come down for the product {product['name']} from {product['current_price']} to {new_price[1]}.Please Visit Store {product['url']} to buy the product")
            elif(float(new_price[1]) < product['set_price']):
                current_track.current_price = float(new_price[1])
                send_email(user.email,"Congratulations ! Price Has Come Down Even Below Your Desired Price ", f"Hi {user.name} the price has come down for the product {product['name']} from {product['current_price']} to {new_price[1]}.Please Visit Store {product['url']} to buy the product")
            else:
                current_track.current_price = product['current_price']
        else:
            price = officeWorks(product['url'])
            print(price)
            new_price = price['price'].split("$")
            if (float(new_price[1]) < product['current_price']):
                current_track.current_price = float(new_price[1])
                send_email(user.email,"Congratulations ! Price Has Come Down Low ", f"Hi {user.name} the price has come down for the product {product['name']} from {product['current_price']} to {new_price[1]}.Please Visit Store {product['url']} to buy the product")
            elif (float(new_price[1]) == product['set_price']):
                current_track.current_price = float(new_price[1])
                send_email(user.email,"Congratulations ! Price Has Come Down To Your Desired Price ", f"Hi {user.name} the price has come down for the product {product['name']} from {product['current_price']} to {new_price[1]}.Please Visit Store {product['url']} to buy the product")
            elif (float(new_price[1]) < product['set_price']):
                current_track.current_price = float(new_price[1])
                send_email(user.email,"Congratulations ! Price Has Come Down Even Below Your Desired Price ", f"Hi {user.name} the price has come down for the product {product['name']} from {product['current_price']} to {new_price[1]}.Please Visit Store {product['url']} to buy the product")
            else:
                current_track.current_price = product['current_price']
        db.session.commit()


