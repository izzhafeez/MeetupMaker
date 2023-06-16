import Location from "../location/Location"

async function getLocations() {
  try {
    const baseLink = process.env.REACT_APP_SERVER_HOST;
    const response = await fetch(baseLink + "/locations");
    const data = await response.json();
    return data;
  } catch (error) {
    console.log(error);
  }
}

const Locations = ({ locations=getLocations() }) => {
  return (
    <ol>
      {locations.map(location => {
        return <Location location={location}/>
      })}
    </ol>
  )
};

export default Locations;