import Meetup from "../meetup/Meetup";

const Meetups = ({ meetups }) => {
  return <div>
    {meetups.map(meetup => {
      return <Meetup meetup={meetup}/>
    })}
  </div>;
};

export default Meetups;