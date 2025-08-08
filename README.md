# FaceFusion
Open Source Video Face Swap Application - AI-powered face swapping using React + Roop engine

# FaceFusion - Open Source Video Face Swap Application

![FaceFusion Logo](https://via.placeholder.com/400x200/0D1117/00A3FF?text=FaceFusion)

[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/facefusion?style=social)](https://github.com/YOUR_USERNAME/facefusion)
[![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/facefusion?style=social)](https://github.com/YOUR_USERNAME/facefusion)
[![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/facefusion)](https://github.com/YOUR_USERNAME/facefusion/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**FaceFusion** is a modern, open-source video face swap web application that uses the powerful [Roop](https://github.com/s0md3v/roop) engine to create stunning face swap videos. Built with React, TypeScript, Tailwind CSS, and Supabase.

> 🌟 **Star this repository** if you find it useful! It helps others discover the project.

## 🎆 Features

- **🤖 AI-Powered Face Swapping**: Uses the advanced Roop engine for high-quality results
- **📹 Multi-Format Support**: Supports MP4, AVI, MOV videos up to 500MB
- **🖼️ Image Compatibility**: Works with JPG, PNG, WEBP images up to 50MB
- **📊 Real-Time Progress**: Live progress tracking with detailed status updates
- **📱 Mobile Responsive**: Beautiful interface that works on all devices
- **🌌 Modern UI**: Dark theme with neon blue accents and smooth animations
- **⚡ Fast Processing**: Optimized workflow with efficient file handling
- **🔒 Secure**: Built-in file validation and automatic cleanup
- **📦 Easy Deployment**: Complete Docker setup for local deployment

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and pnpm
- Supabase account (for backend)
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/facefusion.git
   cd facefusion
   ```

2. **Install dependencies**
   ```bash
   pnpm install
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your Supabase credentials
   ```

4. **Start development server**
   ```bash
   pnpm dev
   ```

5. **Visit the application**
   Open [http://localhost:5173](http://localhost:5173) in your browser

## 🛠️ Backend Setup

### Supabase Configuration

1. **Create a new Supabase project** at [supabase.com](https://supabase.com)

2. **Set up the database schema**
   ```sql
   -- Copy and run the SQL from supabase/migrations/
   ```

3. **Create storage buckets**
   - `source-images` (for face images)
   - `target-videos` (for input videos)
   - `output-videos` (for processed results)

4. **Deploy Edge Functions**
   ```bash
   supabase functions deploy process-face-swap
   ```

5. **Configure environment variables**
   ```bash
   # In your .env file
   VITE_SUPABASE_URL=https://your-project.supabase.co
   VITE_SUPABASE_ANON_KEY=your-anon-key
   SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
   ```

### Roop Installation (Server-side)

The Edge Function automatically installs Roop when first run. For manual installation:

```bash
# Install Python dependencies
apt-get update
apt-get install -y python3 python3-pip git ffmpeg

# Clone Roop
git clone https://github.com/s0md3v/roop.git
cd roop
pip3 install -r requirements.txt
```

## 💫 Usage

1. **Upload Files**
   - Drag and drop a clear face image (source)
   - Drag and drop a video file (target)

2. **Start Processing**
   - Click "Start Face Swap"
   - Monitor real-time progress

3. **Download Results**
   - Preview the processed video
   - Download your face-swapped video
   - Share or create another swap

### Tips for Best Results

- Use high-quality, well-lit photos for source faces
- Ensure faces are clearly visible and front-facing
- Target videos with clear subjects work best
- Processing time varies based on video length and quality

## 📜 Project Structure

```
facefusion/
├── src/
│   ├── components/          # React components
│   │   ├── ui/              # Reusable UI components
│   │   ├── FileUploadZone.tsx
│   │   ├── ProcessingView.tsx
│   │   └── ResultView.tsx
│   ├── lib/
│   │   └── supabase.ts      # Supabase client & API
│   ├── App.tsx              # Main application
│   └── index.css            # Global styles
├── supabase/
│   ├── functions/           # Edge Functions
│   │   └── process-face-swap/
│   └── migrations/          # Database schema
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
└── docs/                    # Documentation
```

## 🐋 Docker Deployment

### Using Docker Compose (Recommended)

```bash
# Build and run with Docker Compose
docker-compose up -d

# Access at http://localhost:3000
```

### Manual Docker Build

```bash
# Build the image
docker build -t facefusion .

# Run the container
docker run -p 3000:3000 -e VITE_SUPABASE_URL=your-url facefusion
```

## 🔧 Development

### Available Scripts

```bash
pnpm dev          # Start development server
pnpm build        # Build for production
pnpm preview      # Preview production build
pnpm lint         # Run ESLint
pnpm type-check   # Run TypeScript checks
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `VITE_SUPABASE_URL` | Your Supabase project URL | Yes |
| `VITE_SUPABASE_ANON_KEY` | Supabase anonymous key | Yes |
| `SUPABASE_SERVICE_ROLE_KEY` | Service role key for Edge Functions | Yes |
| `VITE_DEBUG_MODE` | Enable debug logging | No |

## 📊 Performance

- **Upload Speed**: Parallel file uploads with progress tracking
- **Processing**: Optimized Roop integration with frame-by-frame progress
- **Storage**: Efficient file management with automatic cleanup
- **UI**: Smooth animations and responsive design
- **Bundle Size**: Code splitting and lazy loading

## 🆘 API Reference

### Edge Functions

#### `process-face-swap`
- **POST** `/functions/v1/process-face-swap`
- **Body**: `{ jobId: string }`
- **Response**: Processing status and result URL

### Database Schema

#### `face_swap_jobs`
- Tracks processing jobs and status
- Real-time updates via Supabase Realtime

#### `processing_logs`
- Detailed logs for debugging and monitoring

## 🔒 Security

- **File Validation**: Strict file type and size checking
- **RLS Policies**: Row-level security for data isolation
- **CORS Protection**: Proper CORS headers for API security
- **Input Sanitization**: All inputs validated and sanitized
- **Automatic Cleanup**: Temporary files removed after processing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow TypeScript best practices
- Use conventional commit messages
- Add tests for new features
- Update documentation
- Ensure accessibility compliance

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Roop](https://github.com/s0md3v/roop)** - The powerful face swapping engine
- **[Supabase](https://supabase.com)** - Backend infrastructure
- **[React](https://reactjs.org)** - Frontend framework
- **[Tailwind CSS](https://tailwindcss.com)** - Styling framework
- **[Lucide](https://lucide.dev)** - Icon library

## 📞 Support

If you have questions or need help:

- 📚 [Documentation](docs/)
- 🐛 [Issues](https://github.com/your-username/facefusion/issues)
- 💬 [Discussions](https://github.com/your-username/facefusion/discussions)

## 🎆 Roadmap

- [ ] Batch processing for multiple videos
- [ ] Advanced face detection options
- [ ] Video quality settings
- [ ] Custom model training
- [ ] API webhooks
- [ ] Mobile app

---

**Made with ❤️ using open source technology**

Built by the community, for the community. Star ⭐ this repo if you find it useful!
