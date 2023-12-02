import streamlit as st



#Defining the Baking App
def bakingapp():
            
    st.set_page_config(page_title="Biochemist's Bake's", page_icon="🍰", layout="wide")
    st.markdown(color_theme, unsafe_allow_html=True)

    st.title("Biochemist's Bake's") #new streamlit method adding a title
    select_recipe = st.sidebar.selectbox("Recipes", list(recipes.keys()))
    
    st.subheader(select_recipe)
    display_recipe(select_recipe)

def show_recipe(recipe_name):
    recipe = recipes[recipe_name]

    st.markdown("**Ingredients:**")
    for ingredient in recipe["Ingredients"]:
        st.write(f"- {ingredient}")
    
    st.markdown("**Instructions:**")
    for i, instruction in enumerate(recipe["Instructions"], start=1):
        st.write(f"{i}. {instruction}")
        
if __name__ == "__bakingapp__":
    bakingapp()


recipes = {
    "Lavender Lemon Madeleines": {
        "Ingredients": [
            "1 cup all-purpose flour",
            "1/2 cup unsalted butter, melted",
            "1/2 cup granulated sugar",
            "2 large eggs",
            "1 tablespoon culinary dried lavender flowers",
            "Zest of 1 lemon",
            "1/2 teaspoon baking powder",
            "Pinch of salt",
        ],
        "Instructions": [
            "Preheat the oven to 350°F",
            "In a large bowl, whisk together melted butter, sugar, and eggs until well combined.",
            "Add flour, baking powder, salt, lavender, and lemon zest. Mix until smooth.",
            "Spoon the batter into madeleine molds, be careful not to overfill, the batter will expand a lot in the oven.",
            "Bake for 12-15 minutes or until edges are golden brown.",
            "Allow the madeleines to cool before serving.",
        ],
    },
    "Brown Butter Sea-Salt Chocolate Chip Cookies": {
        "Ingredients": [
            "2 sticks (1 cup) unsalted butter",
            "1 1/2 cups packed dark brown sugar",
            "1/2 cup granulated sugar",
            "1 large egg + 1 egg yolk",
            "2 teaspoons vanilla extract",
            "2 1/4 cups all-purpose flour",
            "1 teaspoon baking soda",
            "1/2 teaspoon sea salt, more for sprinkling",
            "1 tablespoon plain greek yoghurt"
            "3/4 cup semi-sweet chocolate chips",
            "3/4 cup dark chocolate chips",
        ],
        "Instructions": [
            "Preheat the oven to 350°F",
            "In a saucepan, melt butter over medium heat. Consistently stir the butter until it turns a dark amber color., Let it cool for five to ten minutes.",
            "In a large bowl, mix together browned butter, brown sugar, and granulated sugar.",
            "Add eggs and vanilla extract.",
            "In a separate bowl, whisk together flour, baking soda, and sea salt.",
            "Gradually add the dry ingredients intto the wet, mix until combined.",
            "Fold in the chocolate chips.",
            "Cover the dough and let cool in the fridge for at least an hour",
            "Once ready to bake, form the dough into balls of about a tablespoon and a half each.",
            "Bake for 9-12 minutes just letting the edges get golden brown.",
            "Sprinkle cookies with sea salt and enjoy.",
            "(baking tip: to make the cookies look even better, press some chocolate chips onto the tops of the cookies when they are fresh out of the oven."
                    
        ],
    },
    "Frosted Pumpkin Bread": {
        "Ingredients": [
            "1 3/4 cups all-purpose flour",
            "1 teaspoon baking soda",
            "1/2 teaspoon salt",
            "1/2 teaspoon cinnamon",
            "1/4 teaspoon nutmeg",
            "1/4 teaspoon cloves",
            "1/2 cup unsalted butter, softened",
            "1 1/2 cups granulated sugar",
            "2 large eggs",
            "1 cup canned pumpkin puree",
            "1/3 cup water",
            "1/2 teaspoon vanilla extract",
            "For the frosting: 1 cup powdered sugar, 2 tablespoons milk, 1/2 teaspoon vanilla extract",
        ],
        "Instructions": [
            "Preheat the oven to 350°F (175°C).",
            "In a bowl, whisk together flour, baking soda, salt, and spices.",
            "In another bowl, cream together softened butter and sugar until light and fluffy.",
            "Add eggs one at a time, beating well after each addition.",
            "Mix in pumpkin puree, water, and vanilla extract.",
            "Gradually add the dry ingredients to the wet ingredients, mixing until just combined.",
            "Pour the batter into a greased loaf pan and bake for 60-70 minutes or until a toothpick comes out clean.",
            "Allow the pumpkin bread to cool completely before frosting.",
            "For the frosting, mix together powdered sugar, milk, and vanilla extract. Spread over the cooled pumpkin bread.",
        ],
    },
}
