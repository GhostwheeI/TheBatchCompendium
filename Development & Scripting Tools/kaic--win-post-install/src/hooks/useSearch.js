import { useState, useMemo } from 'react';

/**
 * Custom hook for searching/filtering software catalog
 * @param {Array} items - Array of items to search through
 * @param {string} searchKey - The property to search on (e.g., 'name', 'description')
 * @returns {object} - Returns { searchTerm, setSearchTerm, filteredItems }
 */
export const useSearch = (items, searchKeys = ['name', 'description']) => {
  const [searchTerm, setSearchTerm] = useState('');

  const filteredItems = useMemo(() => {
    if (!searchTerm.trim()) {
      return items;
    }

    const lowerSearchTerm = searchTerm.toLowerCase();

    return items.filter((item) => {
      return searchKeys.some((key) => {
        const value = item[key];
        if (typeof value === 'string') {
          return value.toLowerCase().includes(lowerSearchTerm);
        }
        if (Array.isArray(value)) {
          return value.some((v) =>
            String(v).toLowerCase().includes(lowerSearchTerm)
          );
        }
        return false;
      });
    });
  }, [items, searchTerm, searchKeys]);

  return {
    searchTerm,
    setSearchTerm,
    filteredItems,
  };
};
