/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    domains: ["logowik.com"],
    remotePatterns: [
      {
        protocol: "https",
        hostname: "logowik.com",
        pathname: "/content/uploads/images/**",
      },
    ],
  },
};
export default nextConfig;
