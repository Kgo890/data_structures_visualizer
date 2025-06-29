import { Container, Grid, Typography } from "@mui/material";
import React from "react";
import categories from "../data.json";
import Card from "../components/Card";

export default function Home() {
  return (
    <>
      <Container>
        {categories.map((category) => (
          <>
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
                <Card model={model} />
              ))}
            </Grid>
          </>
        ))}
      </Container>
    </>
  );
}