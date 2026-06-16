import { useMemo } from 'react';
import { useSelection } from '../context/SelectionContext';
import { generateBatchScript } from '../generators/bat-generator';

/**
 * Custom hook for script generation and download/copy functionality
 */
export const useScriptGenerator = () => {
  const { selectedSoftware, selectedConfigs } = useSelection();

  // Generate script based on selections
  const generatedScript = useMemo(() => {
    return generateBatchScript(selectedSoftware, selectedConfigs);
  }, [selectedSoftware, selectedConfigs]);

  // Download script as file
  const downloadScript = () => {
    const filename = 'windows-post-install.bat';

    // Add BOM for .bat files (UTF-8 with BOM)
    const content = '\uFEFF' + generatedScript;

    const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);

    return true;
  };

  // Copy script to clipboard
  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(generatedScript);
      return true;
    } catch (err) {
      console.error('Failed to copy to clipboard:', err);

      // Fallback: Try using deprecated execCommand
      try {
        const textArea = document.createElement('textarea');
        textArea.value = generatedScript;
        textArea.style.position = 'fixed';
        textArea.style.opacity = '0';
        document.body.appendChild(textArea);
        textArea.select();
        const success = document.execCommand('copy');
        document.body.removeChild(textArea);
        return success;
      } catch (fallbackErr) {
        console.error('Fallback copy also failed:', fallbackErr);
        return false;
      }
    }
  };

  return {
    generatedScript,
    downloadScript,
    copyToClipboard,
  };
};
