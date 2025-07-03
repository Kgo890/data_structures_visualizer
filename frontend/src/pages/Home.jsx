import { Container, Grid, Typography } from "@mui/material";
import React from "react";
import categories from "../data.json";
import Card from "../components/Card";

export default function Home({ searchQuery }) {
  const searchLower = searchQuery.toLowerCase();
  const searchAsNumber = parseFloat(searchQuery);
  const isNumeric = !isNaN(searchAsNumber);
  const isWhole = isNumeric && Number.isInteger(searchAsNumber);

  const filteredCategories = categories
    .map((category) => {
      const filteredModels = category.models.filter((model) => {
        const matchesName = model.name.toLowerCase().includes(searchLower);
        const matchesDescription = model.description.toLowerCase().includes(searchLower);

        let matchesRating = false;
        if (isNumeric) {
          if (isWhole) {
            matchesRating = model.rating === searchAsNumber || model.rating === searchAsNumber + 0.5;
          } else {
            matchesRating = model.rating === searchAsNumber;
          }
        }

        return matchesName || matchesDescription || matchesRating;
      });

      return { ...category, models: filteredModels };
    })
    .filter((category) => category.models.length > 0);

  return (
    <Container>
      {filteredCategories.map((category) => (
        <div key={category.name}>
          <Typography
            variant="h4"
            component="h2"
            marginBottom={3}
            marginTop={5}
          >
            {category.name} models
          </Typography>
          <Grid container spacing={5}>
            {category.models.map((model) => (
              <Card key={model.name} model={model} />
            ))}
          </Grid>
        </div>
      ))}
    </Container>
  );
}
