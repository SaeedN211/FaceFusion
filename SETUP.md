# FaceFusion Setup Guide

This guide will help you set up FaceFusion locally and deploy it for sharing with friends.

## 🎨 Quick Start (Demo Mode)

The fastest way to try FaceFusion:

```bash
# Clone the repository
git clone https://github.com/SaeedN211/facefusion.git
cd facefusion

# Install dependencies
pnpm install

# Start in demo mode (no backend required)
pnpm dev
```

The app will run in demo mode at http://localhost:5173

## 🛠️ Full Setup (With Backend)

### Step 1: Create Supabase Project

1. Go to [supabase.com](https://supabase.com) and create a new project
2. Wait for the project to be ready (takes a few minutes)
3. Note down your project URL and anon key from Settings > API

### Step 2: Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your Supabase credentials
# VITE_SUPABASE_URL=https://your-project.supabase.co
# VITE_SUPABASE_ANON_KEY=your-anon-key
```

### Step 3: Set Up Database

```bash
# Install Supabase CLI
npm install -g supabase

# Login to Supabase
supabase login

# Link to your project
supabase link --project-ref your-project-id

# Run migrations
supabase db push
```

Or manually run the SQL from `supabase/migrations/001_initial_schema.sql` in your Supabase dashboard.

### Step 4: Create Storage Buckets

In your Supabase dashboard, go to Storage and create these buckets:

1. **source-images** (public, 50MB limit)
2. **target-videos** (public, 500MB limit) 
3. **output-videos** (public, 500MB limit)

### Step 5: Deploy Edge Functions

```bash
# Deploy the face swap processing function
supabase functions deploy process-face-swap

# Set environment variables for the function
supabase secrets set SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
```

### Step 6: Start Development

```bash
# Start the development server
pnpm dev

# Build for production
pnpm build
```

## 🐋 Docker Deployment

### Option 1: Docker Compose (Recommended)

```bash
# Create .env file with your Supabase credentials
cp .env.example .env

# Build and run
docker-compose -f docker/docker-compose.yml up -d

# Access at http://localhost:3000
```

### Option 2: Manual Docker

```bash
# Build the image
docker build -f docker/Dockerfile -t facefusion .

# Run the container
docker run -p 3000:80 \
  -e VITE_SUPABASE_URL=your-url \
  -e VITE_SUPABASE_ANON_KEY=your-key \
  facefusion
```

## 🔧 Development Setup

### Prerequisites

- Node.js 18+
- pnpm (recommended) or npm
- Git

### Installation

```bash
# Install pnpm if you don't have it
npm install -g pnpm

# Install dependencies
pnpm install

# Install Supabase CLI
pnpm add -g supabase
```

### Available Scripts

```bash
pnpm dev          # Start development server
pnpm build        # Build for production
pnpm preview      # Preview production build
pnpm lint         # Run ESLint
pnpm type-check   # Run TypeScript checks
pnpm clean        # Clean build artifacts
```

## 🚫 Troubleshooting

### Common Issues

**Demo mode only**: If you see "Demo Mode Active", your Supabase credentials aren't configured.

**Upload fails**: Check your Supabase storage buckets are created and have correct permissions.

**Processing doesn't start**: Ensure your Edge Function is deployed and environment variables are set.

**Build errors**: Try deleting `node_modules` and running `pnpm install` again.

### Debug Mode

Enable debug logging:

```bash
# In your .env file
VITE_DEBUG_MODE=true
```

### Logs

Check logs in:
- Browser console for frontend issues
- Supabase dashboard > Edge Functions for backend issues
- Docker logs: `docker logs facefusion`

## 📚 File Structure

```
facefusion/
├── src/                     # Frontend source code
│   ├── components/          # React components
│   ├── lib/                 # Utilities and Supabase client
│   └── App.tsx              # Main app component
├── supabase/                # Backend configuration
│   ├── functions/           # Edge Functions
│   └── migrations/          # Database migrations
├── docker/                  # Docker configuration
├── public/                  # Static assets
└── docs/                    # Documentation
```

## 🔒 Security Notes

- Never commit your `.env` file
- Use Supabase RLS policies for data security
- Implement file size and type validation
- Consider rate limiting for production use
- Regularly update dependencies

## 📱 Sharing with Friends

### Option 1: Source Code Sharing

```bash
# Create a zip file
zip -r facefusion-source.zip . -x "node_modules/*" ".git/*" "dist/*"

# Share the zip file with setup instructions
```

### Option 2: Docker Image

```bash
# Build and save Docker image
docker build -f docker/Dockerfile -t facefusion .
docker save facefusion > facefusion-docker.tar

# Friends can load the image
docker load < facefusion-docker.tar
docker run -p 3000:80 facefusion
```

### Option 3: Deploy to Cloud

- **Vercel**: Connect your GitHub repo for automatic deployment
- **Netlify**: Drag and drop your `dist` folder
- **Railway**: One-click deployment with GitHub integration

## ❓ Need Help?

1. Check the [README.md](README.md) for detailed documentation
2. Look at [common issues](docs/troubleshooting.md)
3. Open an issue on GitHub
4. Join our Discord community (link in README)

## 📝 Next Steps

After setup:

1. Test with sample images and videos
2. Configure custom domains if deploying
3. Set up monitoring and analytics
4. Consider adding authentication for production use
5. Implement usage quotas if needed

Enjoy creating amazing face swap videos! 🎆
