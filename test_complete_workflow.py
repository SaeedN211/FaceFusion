#!/usr/bin/env python3
"""
Complete End-to-End Test for FaceFusion
Tests the entire workflow: upload -> process -> download
"""

import os
import sys
import time
import requests
import json
from pathlib import Path

# Configuration
ROOP_SERVICE_URL = "http://localhost:8000"
SUPABASE_URL = os.getenv('SUPABASE_URL', 'https://demo-project.supabase.co')
SUPABASE_ANON_KEY = os.getenv('SUPABASE_ANON_KEY', 'demo-key')

def test_roop_service_health():
    """Test if Roop service is running"""
    print("🔍 Testing Roop service health...")
    try:
        response = requests.get(f"{ROOP_SERVICE_URL}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Roop service is healthy")
            return True
        else:
            print(f"❌ Roop service unhealthy: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Roop service not reachable: {e}")
        return False

def create_test_files():
    """Create test files for face swap"""
    print("📁 Creating test files...")
    
    test_dir = Path("test_files")
    test_dir.mkdir(exist_ok=True)
    
    # Create a simple test image (1x1 pixel JPEG)
    test_image_path = test_dir / "test_face.jpg"
    # Simple JPEG header + minimal data
    jpeg_data = bytes.fromhex('ffd8ffe000104a46494600010101006000600000ffdb004300080606070605080707070909080a0c140d0c0b0b0c1912130f141d1a1f1e1d1a1c1c20242e2720222c231c1c2837292c30313434341f27393d38323c2e333432ffdb0043010909090c0b0c180d0d1832211c213232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232ffc00011080001000103012200021101031101ffc4001f0000010501010101010100000000000000000102030405060708090a0bffc400b5100002010303020403050504040000017d01020300041105122131410613516107227114328191a1082342b1c11552d1f02433627282090a161718191a25262728292a3435363738393a434445464748494a535455565758595a636465666768696a737475767778797a838485868788898a92939495969798999aa2a3a4a5a6a7a8a9aab2b3b4b5b6b7b8b9bac2c3c4c5c6c7c8c9cad2d3d4d5d6d7d8d9dae1e2e3e4e5e6e7e8e9eaf1f2f3f4f5f6f7f8f9faffc4001f0100030101010101010101010000000000000102030405060708090a0bffc400b51100020102040403040705040400010277000102031104052131061241510761711322328108144291a1b1c109233352f0156272d10a162434e125f11718191a262728292a35363738393a434445464748494a535455565758595a636465666768696a737475767778797a82838485868788898a92939495969798999aa2a3a4a5a6a7a8a9aab2b3b4b5b6b7b8b9bac2c3c4c5c6c7c8c9cad2d3d4d5d6d7d8d9dae2e3e4e5e6e7e8e9eaf2f3f4f5f6f7f8f9faffda000c03010002110311003f00ffd9')
    
    with open(test_image_path, 'wb') as f:
        f.write(jpeg_data)
    
    # Create a simple test video (minimal MP4)
    test_video_path = test_dir / "test_video.mp4"
    # Minimal MP4 header
    mp4_data = bytes.fromhex('000000206674797069736f6d0000020069736f6d69736f326d703431')
    
    with open(test_video_path, 'wb') as f:
        f.write(mp4_data)
    
    print(f"✅ Created test files:")
    print(f"   - {test_image_path} ({len(jpeg_data)} bytes)")
    print(f"   - {test_video_path} ({len(mp4_data)} bytes)")
    
    return test_image_path, test_video_path

def test_roop_processing(image_path, video_path):
    """Test the Roop processing service directly"""
    print("🔄 Testing Roop processing service...")
    
    try:
        # Prepare files
        files = {
            'source_image': open(image_path, 'rb'),
            'target_video': open(video_path, 'rb')
        }
        
        # Start processing
        print("   Submitting job to Roop service...")
        response = requests.post(f"{ROOP_SERVICE_URL}/process", files=files)
        
        files['source_image'].close()
        files['target_video'].close()
        
        if response.status_code != 200:
            print(f"❌ Failed to submit job: {response.status_code} - {response.text}")
            return False
        
        result = response.json()
        job_id = result.get('job_id')
        
        if not job_id:
            print(f"❌ No job ID returned: {result}")
            return False
        
        print(f"   Job submitted successfully: {job_id}")
        
        # Monitor progress
        print("   Monitoring progress...")
        max_attempts = 60  # 1 minute timeout
        
        for attempt in range(max_attempts):
            status_response = requests.get(f"{ROOP_SERVICE_URL}/status/{job_id}")
            
            if status_response.status_code != 200:
                print(f"❌ Failed to get status: {status_response.status_code}")
                return False
            
            status = status_response.json()
            print(f"   Progress: {status['progress']}% - {status['message']}")
            
            if status['status'] == 'completed':
                print("✅ Processing completed successfully!")
                
                # Test download
                download_response = requests.get(f"{ROOP_SERVICE_URL}/download/{job_id}")
                if download_response.status_code == 200:
                    print(f"✅ Download successful ({len(download_response.content)} bytes)")
                    
                    # Cleanup
                    cleanup_response = requests.delete(f"{ROOP_SERVICE_URL}/cleanup/{job_id}")
                    print(f"   Cleanup: {cleanup_response.status_code}")
                    
                    return True
                else:
                    print(f"❌ Download failed: {download_response.status_code}")
                    return False
            
            elif status['status'] == 'failed':
                print(f"❌ Processing failed: {status.get('error', 'Unknown error')}")
                return False
            
            time.sleep(1)
        
        print("❌ Processing timeout")
        return False
        
    except Exception as e:
        print(f"❌ Error testing Roop processing: {e}")
        return False

def test_supabase_integration():
    """Test Supabase integration (if configured)"""
    print("🔗 Testing Supabase integration...")
    
    if 'demo' in SUPABASE_URL.lower():
        print("⚠️  Demo mode detected - Supabase integration skipped")
        return True
    
    try:
        # Test basic connectivity
        headers = {
            'apikey': SUPABASE_ANON_KEY,
            'Content-Type': 'application/json'
        }
        
        response = requests.get(f"{SUPABASE_URL}/rest/v1/face_swap_jobs?limit=1", headers=headers)
        
        if response.status_code == 200:
            print("✅ Supabase connection successful")
            return True
        else:
            print(f"❌ Supabase connection failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing Supabase: {e}")
        return False

def run_complete_test():
    """Run the complete end-to-end test"""
    print("🚀 Starting FaceFusion Complete Workflow Test")
    print("=" * 50)
    
    success_count = 0
    total_tests = 0
    
    # Test 1: Roop Service Health
    total_tests += 1
    if test_roop_service_health():
        success_count += 1
    
    # Test 2: Create test files
    total_tests += 1
    try:
        image_path, video_path = create_test_files()
        success_count += 1
    except Exception as e:
        print(f"❌ Failed to create test files: {e}")
        return
    
    # Test 3: Roop Processing
    total_tests += 1
    if test_roop_processing(image_path, video_path):
        success_count += 1
    
    # Test 4: Supabase Integration
    total_tests += 1
    if test_supabase_integration():
        success_count += 1
    
    # Results
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {success_count}/{total_tests} tests passed")
    
    if success_count == total_tests:
        print("🎉 ALL TESTS PASSED - FaceFusion is working correctly!")
        return True
    else:
        print(f"⚠️  {total_tests - success_count} tests failed - Check configuration")
        return False

if __name__ == "__main__":
    success = run_complete_test()
    sys.exit(0 if success else 1)