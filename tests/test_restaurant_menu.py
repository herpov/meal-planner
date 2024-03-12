from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RestaurantMenu(App):
    def build(self):
        # Sample menu items
        menu_items = [
            {"name": "Spaghetti Carbonara", "price": "$12.99"},
            {"name": "Chicken Alfredo", "price": "$14.99"},
            {"name": "Margherita Pizza", "price": "$10.99"},
            {"name": "Grilled Salmon", "price": "$16.99"},
            {"name": "Caesar Salad", "price": "$8.99"},
        ]

        # Create a BoxLayout to hold menu items
        layout = BoxLayout(orientation='vertical')

        # Iterate through menu items and add labels to the layout
        for item in menu_items:
            item_label = Label(text=f"{item['name']} - {item['price']}", size_hint=(1, None), height=40)
            layout.add_widget(item_label)

        return layout

if __name__ == '__main__':
    RestaurantMenu().run()
