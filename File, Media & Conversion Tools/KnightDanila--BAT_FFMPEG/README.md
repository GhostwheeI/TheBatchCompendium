# BAT_FFMPEG 🎥

## About

Batch script files for FFMPEG (Microsoft Windows and DOS, OS/2 🦄)

This is a collection of batch scripts for converting audio, video, and other media files using FFMPEG. The scripts provide a simple drag-and-drop interface for common media conversion tasks.

## Original Repository

This collection is from [KnightDanila/BAT_FFMPEG](https://github.com/KnightDanila/BAT_FFMPEG)

## How to Use

All these `.bat` files work with drag and drop functionality. Just drag and drop media files onto the desired `.bat` script to perform the conversion or operation.

## Logic

All files have a MAIN Code section where you can find the main command(s) for ffmpeg.exe. This main command is marked with a comment:

```
REM //////////////////// MAIN \\\\\\\\\\\\\\\\\\\\\\\\
```

## Features and Scripts

The collection includes scripts for:

### Video Conversion
- **Video-ToMP4_x264.bat** - Convert video to MP4 using x264 codec
- **Video-ToMKV.bat** - Convert video to MKV container
- **Video-ToAVI_MP4_MKV_Container.bat** - Convert to various containers
- **Video-ToWebM.bat** - Convert video to WebM format
- **MP4-ToMKV.bat** - Convert MP4 to MKV
- **AVI-ToMKV.bat** - Convert AVI to MKV
- **TS-ToMKV.bat** - Convert TS to MKV

### Video Editing
- **Video-CutFast.bat** - Quick cut of videos
- **Video-CutAccurateAndRecode.bat** - Accurate cutting with re-encoding
- **Video-SpeedUp_x2.bat** - Speed up video 2x
- **Video-SpeedUp_x4_Beta.bat** - Speed up video 4x (beta)
- **Video-Repair.bat** - Repair video files
- **Video-FrameFix.bat** - Fix frame issues

### Video to GIF Conversion
- **Video-ToGIF_Fast.bat** - Quick GIF conversion
- **Video-ToGIF_HD.bat** - High quality GIF conversion
- **Video-ToGIF_16Bit-Style.bat** - Retro style GIF with 16-bit color palette
- **Video-ToGIF_32ColorsStyle.bat** - GIF with 32 colors
- **Video-ToGIF_64ColorsStyle.bat** - GIF with 64 colors
- Multiple resolution variants (_240p, _480p, _720p, etc.)
- **Video-ToGIF_FX_Boomerang.bat** - Create boomerang effect GIF

### Video Information & Metadata
- **Video-GetCodecINFO.bat** - Get codec information
- **Video-MetadataChange.bat** - Change video metadata

### Audio Conversion & Editing
- **Audio-ToMP3.bat** - Convert audio to MP3
- **Audio-ToMP3_RemoveSideData.bat** - Convert to MP3 and remove side data
- **Audio-ToAC3_AAC.bat** - Convert audio to AC3 or AAC
- **Audio-ToOGG.bat** - Convert audio to OGG
- **Audio-AudioGain.bat** - Adjust audio gain
- **Audio-GetInfo.bat** - Get audio information
- **Audio-CutAccurateAndRecode.bat** - Cut and re-encode audio
- **MP3-ToWav.bat** - Convert MP3 to WAV

### Subtitle Management
- **Video-SubAdd.bat** - Add subtitles to video
- **Video-SubGet.bat** - Extract subtitles from video
- **Video-SubGetByNum.bat** - Extract specific subtitle track by number

### YouTube-DL Integration
Multiple scripts for downloading content from YouTube and other platforms:
- **youtube-dl-Video-1080p-FPS30.bat** - Download 1080p video at 30 FPS
- **youtube-dl-Video-720p.bat** - Download 720p video
- **youtube-dl-Video-480p-FPS30.bat** - Download 480p video at 30 FPS
- **youtube-dl-MP3-192Kbps.bat** - Download and convert to MP3 (192 Kbps)
- **youtube-dl-OGG-192Kbps.bat** - Download and convert to OGG (192 Kbps)
- **youtube-dl-Video-Sub.bat** - Download video with subtitles
- With thumbnail options and split-by-chapters variants

### Image Conversion
- **Video-ToJPG.bat** - Extract frames as JPG images
- **Video-ToBMP.bat** - Extract frames as BMP images
- **WebM-WebP-ToJPG.bat** - Convert WebM/WebP to JPG
- **WebM-WebP-ToPNG.bat** - Convert WebM/WebP to PNG
- **WebM-WebP-ToGIF.bat** - Convert WebM/WebP to GIF

### Video Adjustments
- **Video-Volume.bat** - Adjust video volume
- **DND_CropBottom.bat** - Crop bottom of video (drag and drop)
- **DND_Rotate.bat** - Rotate video (drag and drop)
- **DND_Zoom.bat** - Zoom video (drag and drop)
- **Video-AudioRemove.bat** - Remove audio track
- **Video_Upscale_QHD.bat** - Upscale video to QHD resolution

### Special Tools
- **Icon_iOS_Generator.bat** - Generate iOS app icons
- **Version-of-ffmpeg.bat** - Check FFMPEG version
- **Version-of-youtube-dl.bat** - Check youtube-dl version
- **GitUpdate.bat** - Update the repository

## Included Tools

The scripts use the following bundled tools:
- ffmpeg.exe - Main video/audio conversion tool
- ffplay.exe - Media player
- ffprobe.exe - Media information tool
- youtube-dl.exe - YouTube and online video downloader
- ImageMagick_convert.exe - Image conversion tool
- AtomicParsley.exe - Metadata tagging tool
- lf2crlf.exe - Line ending conversion utility

## Requirements

- Windows operating system
- The included executables (ffmpeg, youtube-dl, etc.) must be in the same directory as the batch files

## Notes

⚠️ These scripts are designed for Microsoft Windows and DOS/OS/2 systems. The batch files modify and process media files - always keep backups of your original files before processing.

All output files are typically created in a subdirectory or alongside the original files, depending on the specific script.
