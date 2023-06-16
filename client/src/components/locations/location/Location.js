const Location = ({ location }) => {
  const lat = location.coords.lat;
  const lng = location.coords.lng;

  return (
    <div className="border-primary">
      <h4>{location.name}</h4>
      <p>({lat}, {lng})</p>
    </div>
  )
};

export default Location;