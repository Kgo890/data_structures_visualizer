import {
  createTheme,
  Grid,
  Paper,
  Rating,
  ThemeProvider,
  Typography,
} from "@mui/material";
import { Box } from "@mui/system";
import React from "react";
import { useNavigate } from "react-router-dom";

const theme = createTheme({
  components: {
    MuiTypography: {
      variants: [
        {
          props: { variant: "body2" },
          style: { fontSize: 11 },
        },
        {
          props: { variant: "body3" },
          style: { fontSize: 9 },
        },
      ],
    },
  },
});

export default function Card({ model }) {
  const navigate = useNavigate();

  const handleClick = () => {
    if (model.route) {
      navigate(model.route);
    }
  };

  return (
    <Grid item xs={12} sm={6} md={4} lg={3} onClick={handleClick} style={{ cursor: "pointer" }}>
      <ThemeProvider theme={theme}>
        <Paper elevation={3} className="paper">
          <img
            src={model.image}
            alt={model.name}
            className="img"
            onError={(e) => {
              e.target.onerror = null;
              e.target.src = "/assets/default.png";
            }}
          />
          <Box sx={{ paddingX: 1, paddingY: 2 }}>
            <Typography variant="subtitle1" component="h2" gutterBottom>
              {model.name}
            </Typography>
            <Typography variant="body2" color="textSecondary" gutterBottom>
              {model.description}
            </Typography>
            <Box sx={{ display: "flex", alignItems: "center", marginTop: 1 }}>
              <Rating
                name="read-only-rating"
                size="small"
                defaultValue={model.rating}
                precision={0.5}
                readOnly
              />
              <Typography variant="body2" component="span" marginLeft={0.5}>
                {model.rating}
              </Typography>
            </Box>
          </Box>
        </Paper>
      </ThemeProvider>
    </Grid>
  );
}
