import { Container, Grid, Typography } from "@mui/material";
import React from "react";
import categories from "../data.json";
import Card from "../components/Card";

export default function Home({ searchQuery }) {
  const filteredCategories = categories.map((category) => {
    const filteredModels = category.models.filter((model) =>
      model.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      model.description.toLowerCase().includes(searchQuery.toLowerCase())
    );
    return { ...category, models: filteredModels };
  }).filter(category => category.models.length > 0);

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
