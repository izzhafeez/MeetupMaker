import { useEffect, useState } from "react";

import Locations from "../components/locations";

const Home = () => {
  const locationsDetails = [
    {
      name: "Helga",
      coords: {
        lat: 2,
        lng: 3
      }
    },
    {
      name: "Hol",
      coords: {
        lat: 3,
        lng: 4
      }
    }
  ];

  return <Locations locations={locationsDetails}/>;
}

export default Home;