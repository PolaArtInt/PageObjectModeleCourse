class URLs:
    base_url = 'https://www.saucedemo.com/v1/'
    login_url = 'https://www.saucedemo.com/v1/index.html'
    inventory_url = 'https://www.saucedemo.com/v1/inventory.html'
    cart_url = 'https://www.saucedemo.com/v1/cart.html'
    checkout_url = 'https://www.saucedemo.com/v1/checkout-complete.html'
    about_url = 'https://saucelabs.com/'
    item_url = 'https://www.saucedemo.com/v1/inventory-item.html'


class AuthData:
    standard_user = 'standard_user'
    locked_user = 'locked_out_user'
    problem_user = 'problem_user'
    glitch_user = 'performance_glitch_user'

    pass_word = 'secret_sauce'

    wrong_user = 'user'
    wrong_password = 'user'


class AuthLocs:
    input_user = ('xpath', '//input[@id="user-name"]')
    input_pass = ('xpath', '//input[@id="password"]')
    login_btn = ('xpath', '//input[@id="login-button"]')

    locked_msg = 'Epic sadface: Sorry, this user has been locked out.'
    login_err_msg = 'Epic sadface: Username and password do not match any user in this service'


class InventoryLocs:
    prod_header = ('xpath', '//div[@class="product_label"]')

    item_cards = ('xpath', '//div[@class="inventory_item"]')
    item_imgs = ('xpath', '//img[@class="inventory_item_img"]')
    item_names = ('xpath', '//div[@class="inventory_item_name"]')
    item_descs = ('xpath', '//div[@class="inventory_item_desc"]')
    item_prices = ('xpath', '//div[@class="inventory_item_price"]')

    add_btns = ('xpath', '//button[@class="btn_primary btn_inventory"]')
    remove_btns = ('xpath', '//button[@class="btn_secondary btn_inventory"]')


class FilterLocs:
    drop_a_z = ('xpath', '//option[@value="az"]')
    drop_z_a = ('xpath', '//option[@value="za"]')
    drop_low_high = ('xpath', '//option[@value="lohi"]')
    drop_high_low = ('xpath', '//option[@value="hilo"]')


class MenuLocs:
    menu_container = ('xpath', '//div[@class="bm-menu"]')
    menu_btn = ('xpath', '//div[@class="bm-burger-button"]//button')
    all_items_btn = ('xpath', '//a[@id="inventory_sidebar_link"]')
    about_btn = ('xpath', '//a[@id="about_sidebar_link"]')
    logout_btn = ('xpath', '//a[@id="logout_sidebar_link"]')
    reset_btn = ('xpath', '//a[@id="reset_sidebar_link"]')
    x_btn = ('xpath', '//div[@class="bm-cross-button"]/button')


class CartLocs:
    cart_header = ('xpath', '//div[@class="subheader"]')
    cart_btn = ('xpath', '//a[@class="shopping_cart_link fa-layers fa-fw"]')
    cart_tag = ('xpath', '//a[@class="shopping_cart_link fa-layers fa-fw"]/span')

    cart = ('xpath', '//div[@id="cart_contents_container"]')
    cart_quantity_num = ('xpath', '//div[@class="cart_quantity"]')
    cart_remove_btn = ('xpath', '//button[@class="btn_secondary cart_button"]')


class ItemLocs:
    card_add_btn = ('xpath', '//button[@class="btn_primary btn_inventory"]')
    card_remove_btn = ('xpath', '//button[@class="btn_secondary btn_inventory"]')

    card_img = ('xpath', '//img[@class="inventory_details_img"]')
    card_name = ('xpath', '//div[@class="inventory_details_name"]')
    card_desc = ('xpath', '//div[@class="inventory_details_desc"]')
    card_price = ('xpath', '//div[@class="inventory_details_price"]')


class OrderLocs:
    input_fname = ('xpath', '//input[@id="first-name"]')
    input_lname = ('xpath', '//input[@id="last-name"]')
    input_zipcode = ('xpath', '//input[@id="postal-code"]')

    checkout_btn = ('xpath', '//a[@class="btn_action checkout_button"]')
    continue_btn = ('xpath', '//input[@class="btn_primary cart_button"]')
    finish_btn = ('xpath', '//a[@class="btn_action cart_button"]')
    cancel_btn = ('xpath', '//a[@class="cart_cancel_link btn_secondary"]')

    complete_msg = 'THANK YOU FOR YOUR ORDER'


class AboutLocs:
    exp_title = 'Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing'
