import Header from "../components/Header";
import MainLayout from "../components/mainlayout";


function Home() {
  return (
    <div className="min-h-screen bg-gray-500 p-3">
      <Header />
        <MainLayout />
    </div>
  );
}

export default Home;