import streamlit as st
import os

# Define the recipe pages with an optional serving size parameter and image
def recipe(name, serving_size=1):
    st.title(name + " Recipe") #1st New Stremalit Methods
    image_filename = os.path.join("images/"+name.lower() + ".jpg") #Will Include 3 Images
    st.image(image_filename, use_column_width=True)
    st.header("Ingredients:")
    if name == "Brown Butter Cookies":
        butter_quantity = 1 * serving_size
        sugar_quantity = 1.5 * serving_size
        st.write(f"- {butter_quantity} cups unsalted butter, browned")
        st.write(f"- {sugar_quantity} cups packed dark brown sugar")
        st.write("- 1 large egg + 1 egg yolk")
        st.write("- 2 teaspoons vanilla extract")
        st.write("- 2 1/4 cups all-purpose flour")
        st.write("- 1 teaspoon baking soda")
        st.write("- 1/2 teaspoon sea salt, more for sprinkling")
        st.write("- 3/4 cup semi-sweet chocolate chips")
        st.write("- 3/4 cup dark chocolate chips")
    elif name == "Lemon Lavender Madeleines":
        flour_quantity = 1 * serving_size
        butter_quantity = 0.5 * serving_size
        sugar_quantity = 0.5 * serving_size
        eggs_quantity = 2 * serving_size
        st.write(f"- {flour_quantity} cup all-purpose flour")
        st.write(f"- {butter_quantity} cup unsalted butter, melted")
        st.write(f"- {sugar_quantity} cup granulated sugar")
        st.write(f"- {eggs_quantity} large eggs")
        st.write("- 1 tablespoon culinary dried lavender flowers")
        st.write("- Zest of 1 lemon")
        st.write("- 1/2 teaspoon baking powder")
        st.write("- Pinch of salt")
    elif name == "Pumpkin Bread":
        flour_quantity = 1.75 * serving_size
        baking_soda_quantity = 1 * serving_size
        salt_quantity = 0.5 * serving_size
        cinnamon_quantity = 0.5 * serving_size
        nutmeg_quantity = 0.25 * serving_size
        cloves_quantity = 0.25 * serving_size
        st.write(f"- {flour_quantity} cups all-purpose flour")
        st.write(f"- {baking_soda_quantity} teaspoon baking soda")
        st.write(f"- {salt_quantity} teaspoon salt")
        st.write(f"- {cinnamon_quantity} teaspoon cinnamon")
        st.write(f"- {nutmeg_quantity} teaspoon nutmeg")
        st.write(f"- {cloves_quantity} teaspoon cloves")
        st.write("- 1/2 cup unsalted butter, softened")
        st.write("- 1 1/2 cups granulated sugar")
        st.write("- 2 large eggs")
        st.write("- 1 cup canned pumpkin puree")
        st.write("- 1/3 cup water")
        st.write("- 1/2 teaspoon vanilla extract")
    st.header("Instructions:")
    if name == "Brown Butter Cookies":
        st.write("1. Preheat the oven to 350°F.")
        st.write("2. In a saucepan, melt butter over medium heat. Stir consistently until it turns a dark amber color. Let it cool for 5-10 minutes.")
        st.write("3. In a large bowl, mix together browned butter, brown sugar, and granulated sugar.")
        st.write("4. Add eggs and vanilla extract.")
        st.write("5. In a separate bowl, whisk together flour, baking soda, and sea salt.")
        st.write("6. Gradually add the dry ingredients to the wet ingredients, mixing until combined.")
        st.write("7. Fold in the chocolate chips.")
        st.write("8. Cover the dough and let it cool in the fridge for at least an hour.")
        st.write("9. Once ready to bake, form the dough into balls of about a tablespoon and a half each.")
        st.write("10. Bake for 9-12 minutes, just letting the edges get golden brown.")
        st.write("11. Sprinkle cookies with sea salt and enjoy!")
        st.write("(Baking tip: to make the cookies look even better, press some chocolate chips onto the tops of the cookies when they are fresh out of the oven.")
    elif name == "Lemon Lavender Madeleines":
        st.write("1. Preheat the oven to 350°F.")
        st.write("2. In a large bowl, whisk together melted butter, sugar, and eggs until well combined.")
        st.write("3. Add flour, baking powder, salt, lavender, and lemon zest. Mix until smooth.")
        st.write("4. Spoon the batter into madeleine molds, being careful not to overfill, as the batter will expand a lot in the oven.")
        st.write("5. Bake for 12-15 minutes or until the edges are golden brown.")
        st.write("6. Allow the madeleines to cool before serving.")
    elif name == "Pumpkin Bread":
        st.write("1. Preheat the oven to 350°F.")
        st.write("2. In a bowl, whisk together flour, baking soda, salt, and spices.")
        st.write("3. In another bowl, cream together softened butter and sugar until light and fluffy.")
        st.write("4. Add eggs one at a time.")
        st.write("5. Mix in pumpkin puree, water, and vanilla extract.")
        st.write("6. Gradually add the dry ingredients to the wet ingredients, mixing until just combined.")
        st.write("7. Pour the batter into a greased or buttered loaf pan and bake for 1 hour or until a toothpick comes out clean.")
        st.write("8. Allow the pumpkin bread to cool completely before frosting.")
