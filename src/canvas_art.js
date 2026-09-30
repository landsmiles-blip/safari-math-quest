window.ArtEngine = {
    renderCertificate: function(canvasId, studentName, score, categoryScores) {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;
        
        // Ensure high-res canvas
        const width = 1000;
        const height = 700;
        
        // Handle DPI scaling
        const dpr = window.devicePixelRatio || 1;
        canvas.width = width * dpr;
        canvas.height = height * dpr;
        
        // Scale down via CSS
        canvas.style.width = width + "px";
        canvas.style.height = height + "px";
        
        const ctx = canvas.getContext("2d");
        ctx.scale(dpr, dpr);
        
        // Clear background with cosmic-pastel gradient
        const bgGradient = ctx.createLinearGradient(0, 0, width, height);
        bgGradient.addColorStop(0, "#0f172a"); // Dark slate blue
        bgGradient.addColorStop(0.5, "#2e1065"); // Deep purple
        bgGradient.addColorStop(1, "#172554"); // Dark blue
        ctx.fillStyle = bgGradient;
        ctx.fillRect(0, 0, width, height);

        // Draw orbital ellipses
        ctx.strokeStyle = "rgba(255, 255, 255, 0.15)";
        ctx.lineWidth = 2;
        for (let i = 0; i < 3; i++) {
            ctx.beginPath();
            ctx.ellipse(width/2, height/2, 400 - (i*50), 200 - (i*30), (Math.PI / 6) * i, 0, 2 * Math.PI);
            ctx.stroke();
        }

        // Draw 4-point sparkle stars
        const drawStar = (x, y, radius) => {
            ctx.fillStyle = "rgba(255, 255, 255, 0.8)";
            ctx.beginPath();
            for (let i = 0; i < 8; i++) {
                const angle = (i * Math.PI) / 4;
                const r = (i % 2 === 0) ? radius : radius / 4;
                const px = x + Math.cos(angle) * r;
                const py = y + Math.sin(angle) * r;
                if (i === 0) ctx.moveTo(px, py);
                else ctx.lineTo(px, py);
            }
            ctx.closePath();
            ctx.fill();
        };

        for (let i = 0; i < 30; i++) {
            drawStar(Math.random() * width, Math.random() * height, Math.random() * 8 + 4);
        }

        // Draw bunting garland at the top
        const drawBunting = () => {
            const numFlags = 15;
            const flagWidth = width / numFlags;
            
            // Garland string
            ctx.beginPath();
            ctx.moveTo(0, 50);
            ctx.quadraticCurveTo(width/2, 100, width, 50);
            ctx.strokeStyle = "rgba(255, 255, 255, 0.5)";
            ctx.lineWidth = 2;
            ctx.stroke();

            // Flags
            for (let i = 0; i < numFlags; i++) {
                const x1 = i * flagWidth;
                const x2 = (i + 1) * flagWidth;
                
                // approximate curve point
                const t1 = i / numFlags;
                const y1 = 50 * Math.pow(1-t1, 2) + 100 * 2 * (1-t1) * t1 + 50 * Math.pow(t1, 2);
                
                const t2 = (i+1) / numFlags;
                const y2 = 50 * Math.pow(1-t2, 2) + 100 * 2 * (1-t2) * t2 + 50 * Math.pow(t2, 2);
                
                const colors = ["#f472b6", "#60a5fa", "#34d399", "#fbbf24"];
                ctx.fillStyle = colors[i % colors.length];
                
                ctx.beginPath();
                ctx.moveTo(x1, y1);
                ctx.lineTo(x2, y2);
                ctx.lineTo((x1 + x2) / 2, Math.max(y1, y2) + 40);
                ctx.closePath();
                ctx.fill();
            }
        };
        drawBunting();

        // Draw Gold Rosette Seal
        const drawSeal = (cx, cy) => {
            const outerRadius = 60;
            const innerRadius = 45;
            const points = 30;
            
            ctx.fillStyle = "#fbbf24";
            
            // Ribbon tails
            ctx.beginPath();
            ctx.moveTo(cx - 20, cy + 40);
            ctx.lineTo(cx - 40, cy + 120);
            ctx.lineTo(cx - 10, cy + 100);
            ctx.lineTo(cx + 20, cy + 120);
            ctx.lineTo(cx, cy + 40);
            ctx.fill();

            // Rosette
            ctx.beginPath();
            for (let i = 0; i < points * 2; i++) {
                const r = (i % 2 === 0) ? outerRadius : innerRadius;
                const angle = (i * Math.PI) / points;
                const px = cx + Math.cos(angle) * r;
                const py = cy + Math.sin(angle) * r;
                if (i === 0) ctx.moveTo(px, py);
                else ctx.lineTo(px, py);
            }
            ctx.closePath();
            ctx.fill();
            
            // Inner gold circle
            ctx.beginPath();
            ctx.arc(cx, cy, 35, 0, Math.PI * 2);
            ctx.fillStyle = "#f59e0b";
            ctx.fill();
            
            // Seal text
            ctx.fillStyle = "#ffffff";
            ctx.font = "bold 16px Arial";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            ctx.fillText("GOLD", cx, cy - 8);
            ctx.fillText("AWARD", cx, cy + 8);
        };
        drawSeal(width - 150, height - 150);
        
        // Add text content
        ctx.shadowColor = "rgba(0,0,0,0.5)";
        ctx.shadowBlur = 10;
        
        ctx.fillStyle = "#ffffff";
        ctx.textAlign = "center";
        
        ctx.font = "italic 40px 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif";
        ctx.fillText("Certificate of Achievement", width / 2, 200);
        
        ctx.font = "bold 60px 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif";
        ctx.fillStyle = "#fbbf24"; // gold text
        ctx.fillText(studentName || "Math Explorer", width / 2, 300);
        
        ctx.fillStyle = "#ffffff";
        ctx.font = "24px 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif";
        ctx.fillText("has successfully completed the Safari Math Quest", width / 2, 380);
        
        ctx.font = "bold 32px 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif";
        ctx.fillText(`Final Score: ${score || 0}`, width / 2, 450);
        
        // Reset shadow for neatness
        ctx.shadowBlur = 0;
        
        // Categories line
        if (categoryScores) {
            ctx.font = "18px 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif";
            ctx.fillStyle = "rgba(255,255,255,0.8)";
            let catStr = Object.entries(categoryScores)
                .map(([cat, val]) => `${cat}: ${val}`)
                .join(" | ");
            ctx.fillText(catStr, width / 2, 520);
        }
    },

    downloadCertificate: function(canvasId) {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;
        
        const dataUrl = canvas.toDataURL('image/png');
        const link = document.createElement('a');
        link.download = 'Safari-Math-Quest-Certificate.png';
        link.href = dataUrl;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
};
