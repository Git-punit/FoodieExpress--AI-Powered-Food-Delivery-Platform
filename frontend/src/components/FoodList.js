import { useEffect, useState } from "react";

function FoodList() {
  const [foods, setFoods] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/foods")
      .then(response => response.json())
      .then(data => setFoods(data));
  }, []);

  return (
    <ul>
      {foods.map(food => (
        <li key={food.id}>
          {food.name} - ₹{food.price}
        </li>
      ))}
    </ul>
  );
}

export default FoodList;
